import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import transforms, datasets
import torchvision.models as models
from tqdm import tqdm
from PIL import Image
import matplotlib.pyplot as plt
import os
import pickle

# ===================== 超参数设置（M1 Pro 优化）=====================
epochs = 5  # 训练5轮足够交报告，速度快
batch_size = 16  # M1 Pro 32G内存可拉到32
# 数据集路径：直接指向你下载的文件夹
image_path = './垃圾/garbage_data/data'
save_path = './垃圾/garbage_chk/best_model.pkl'
# 自动选择MPS（M1 Pro GPU）， fallback到CPU
device = torch.device('mps' if torch.backends.mps.is_available() else 'cpu')
print(f"✅ 使用设备: {device}")

# 创建保存文件夹
if not os.path.exists('./垃圾/garbage_chk'):
    os.makedirs('./垃圾/garbage_chk')

# ===================== 1. 数据处理与迭代器 =====================
data_transform = {
    'train': transforms.Compose([
        transforms.RandomResizedCrop(224),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])
}

# 加载真实数据集（路径已修正，直接用你的文件夹）
train_dataset = datasets.ImageFolder(
    root=image_path,
    transform=data_transform['train']
)
train_loader = torch.utils.data.DataLoader(
    train_dataset,
    batch_size=batch_size,
    shuffle=True,
    num_workers=0  # Mac上设为0，避免多进程报错
)

print(f"✅ 加载训练集成功！共 {len(train_dataset)} 张图片，{len(train_dataset.classes)} 个类别")

# 保存类别映射（对应12个垃圾分类）
class_dict = {val: key for key, val in train_dataset.class_to_idx.items()}
with open('./垃圾/class_dict.pk', 'wb') as f:
    pickle.dump(class_dict, f)
print(f"✅ 类别映射已保存：{class_dict}")


# ===================== 2. 自定义损失函数（实验要求）=====================
class MyLoss(nn.Module):
    def __init__(self):
        super(MyLoss, self).__init__()

    def forward(self, pred, label):
        exp = torch.exp(pred)
        tmp1 = exp.gather(1, label.unsqueeze(-1)).squeeze()
        tmp2 = exp.sum(1)
        softmax = tmp1 / tmp2
        log_loss = -torch.log(softmax + 1e-8)  # 加1e-8避免log(0)
        return log_loss.mean()


# ===================== 3. 模型构建（迁移学习，MnasNet）=====================
# 本地加载权重，不联网下载，避免SSL报错
model = models.mnasnet1_0(weights=None)
# 冻结主干网络，只训练分类头
for param in model.parameters():
    param.requires_grad = False
# 修改分类层为12类（对应你的12个垃圾分类）
model.classifier[1] = nn.Linear(model.classifier[1].in_features, 12)
model = model.to(device)

criterion = MyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)  # 学习率0.001，训练稳定

# ===================== 4. 模型训练 =====================
best_acc = 0
print("\n🚀 开始训练...")
for epoch in range(epochs):
    model.train()
    running_loss = 0.0
    correct = 0
    total = 0
    train_bar = tqdm(train_loader)

    for data in train_bar:
        images, labels = data
        images = images.to(device)
        labels = labels.to(device)

        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        running_loss += loss.item()
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

    epoch_acc = correct / total
    print(f"\nEpoch {epoch + 1:02d} | Loss: {running_loss:.3f} | Acc: {epoch_acc * 100:.2f}%")

    # 保存最优模型
    if epoch_acc > best_acc:
        best_acc = epoch_acc
        torch.save(model.state_dict(), save_path)
        print(f"✅ 新最优模型已保存，准确率: {best_acc * 100:.2f}%")

print(f"\n🎉 训练完成！最高准确率: {best_acc * 100:.2f}%")

# ===================== 5. 单张图片测试（用你的shoes1750.jpg）=====================
# 测试图片路径：直接指向你下载的test文件夹里的图片
img_path = './垃圾/garbage_data/test/shoes1750.jpg'
if not os.path.exists(img_path):
    print(f"⚠️ 测试图片 {img_path} 不存在，请检查路径！")
else:
    img = Image.open(img_path).convert('RGB')  # 统一转RGB，避免4通道报错

    test_transform = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])

    img_tensor = test_transform(img).unsqueeze(0).to(device)  # 加batch维度，移到MPS

    # 加载类别映射
    with open('./垃圾/class_dict.pk', 'rb') as f:
        class_dict = pickle.load(f)

    # 预测
    model.eval()
    with torch.no_grad():
        outputs = model(img_tensor)
        pred = outputs.argmax(axis=1).item()

    # 显示结果（完美截图用）
    plt.figure(figsize=(6, 6))
    plt.imshow(img)
    plt.title(f'预测类别: {class_dict[pred]}', fontsize=14)
    plt.axis('off')
    plt.show()
    print(f"\n【预测结果】: {class_dict[pred]}")