import numpy as np

print("===== 1. 创建数组 =====")

# 从列表创建数组
arr1 = np.array([1, 2, 3, 4, 5])
print("一维数组:", arr1)

# 二维数组（矩阵）
arr2 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print("二维数组:\n", arr2)

# 查看形状
print("arr1 形状:", arr1.shape)   # (5,)  → 5个元素
print("arr2 形状:", arr2.shape)   # (2,3) → 2行3列


print("\n===== 2. 特殊数组 =====")

# 全是0
zeros = np.zeros((3, 3))
print("3x3 全0:\n", zeros)

# 全是1
ones = np.ones((2, 4))
print("2x4 全1:\n", ones)

# 等差数列
range_arr = np.arange(0, 10, 2)  # 从0到10，步长2
print("等差数列:", range_arr)

# 均匀分布
lin = np.linspace(0, 1, 5)  # 0到1之间均匀取5个数
print("均匀5个数:", lin)

# 随机数
rand = np.random.randn(3)  # 3个随机数
print("随机数:", rand)


print("\n===== 3. 数组运算 =====")

a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])

print("a:", a)
print("b:", b)
print("a + b:", a + b)      # 对应元素相加
print("a * b:", a * b)      # 对应元素相乘（不是矩阵乘法）
print("a * 10:", a * 10)    # 标量乘数组（广播）
print("a ** 2:", a ** 2)    # 每个元素平方
print("a > 2:", a > 2)      # 每个元素比较，返回 True/False

# 矩阵乘法
c = np.array([[1, 2], [3, 4]])
d = np.array([[5, 6], [7, 8]])
print("\n矩阵乘法:\n", c @ d)        # @ 才是矩阵乘法


print("\n===== 5. 切片和索引 =====")

arr = np.array([[1, 2, 3, 4], 
                [5, 6, 7, 8], 
                [9, 10, 11, 12]])

print("原始数组:\n", arr)
print("第0行:", arr[0])             # 取一行
print("第1行第2列:", arr[1, 2])     # 取一个元素
print("前2行:\n", arr[:2])          # 取多行
print("前2行前3列:\n", arr[:2, :3]) # 取子区域
print("所有行的第1列:", arr[:, 1])  # 取一整列
