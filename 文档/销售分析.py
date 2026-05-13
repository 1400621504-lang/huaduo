import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["Arial Unicode MS", "SimHei", "PingFang SC"]
plt.rcParams["axes.unicode_minus"] = False

data = pd.DataFrame({
    "日期": pd.date_range("2024-01-01", periods=100, freq="D"),
    "产品": ["A产品", "B产品", "C产品"] * 33 + ["A产品"],
    "销量": [
        30, 45, 20, 35, 50, 28, 42, 55, 18, 38,
        48, 22, 33, 52, 25, 40, 60, 15, 44, 36,
        10, 65, 72, 12, 58, 90, 5, 80, 68, 23,
        30, 45, 20, 35, 50, 28, 42, 55, 18, 38,
        48, 22, 33, 52, 25, 40, 60, 15, 44, 36,
        10, 65, 72, 12, 58, 90, 5, 80, 68, 23,
        30, 45, 20, 35, 50, 28, 42, 55, 18, 38,
        48, 22, 33, 52, 25, 40, 60, 15, 44, 36,
        10, 65, 72, 12, 58, 90, 5, 80, 68, 23,
        30, 45, 20, 35, 50, 28, 42, 55, 18, 36
    ],
    "金额": [
        300, 450, 200, 350, 500, 280, 420, 550, 180, 380,
        480, 220, 330, 520, 250, 400, 600, 150, 440, 360,
        100, 650, 720, 120, 580, 900, 50, 800, 680, 230,
        300, 450, 200, 350, 500, 280, 420, 550, 180, 380,
        480, 220, 330, 520, 250, 400, 600, 150, 440, 360,
        100, 650, 720, 120, 580, 900, 50, 800, 680, 230,
        300, 450, 200, 350, 500, 280, 420, 550, 180, 380,
        480, 220, 330, 520, 250, 400, 600, 150, 440, 360,
        100, 650, 720, 120, 580, 900, 50, 800, 680, 230,
        300, 450, 200, 350, 500, 280, 420, 550, 180, 360
    ]
})


data.loc[10,"销量"] = None
data.loc[25,"金额"] = None
data.loc[50,"销量"] = None
data.loc[60,"金额"] = None

print(f"原始数据前十行:\n{data.head(10)}")
print(f"\n缺失情况:\n{data.isnull().sum()}")

# ===== 2. 清洗数据 =====
df_clean = data.copy()
df_clean["销量"] = df_clean["销量"].fillna(df_clean["销量"].median()).astype(int)
df_clean["金额"] = df_clean["金额"].fillna(df_clean["金额"].median()).astype(int)

# ===== 3. 各产品总销量和总金额 =====
product_sum = df_clean.groupby("产品").agg({"销量": "sum", "金额": "sum"})
print(f"\n各产品销售统计:\n{product_sum}")

# ===== 4. 各产品平均金额 =====
product_mean = df_clean.groupby("产品")["金额"].mean().astype(int)
print(f"\n各产品平均每单金额:\n{product_mean}")

# ===== 5. 按产品画柱状图（总销量）=====
# product_sum["销量"].plot(kind="bar")
# plt.title("各产品总销量")
# plt.ylabel("销量")
# for i, v in enumerate(product_sum["销量"]):
#     plt.text(i, v + 10, str(v), ha="center")
# plt.show()

# # ===== 6. 按产品画饼图（金额占比）=====
# product_sum["金额"].plot(kind="pie", autopct="%.1f%%")
# plt.title("各产品金额占比")
# plt.ylabel("")
# plt.show()
# ===== 5. 柱状图 =====
plt.figure()   # 新建一个图
product_sum["销量"].plot(kind="bar")
plt.title("各产品总销量")
plt.ylabel("销量")
for i, v in enumerate(product_sum["销量"]):
    plt.text(i, v + 10, str(v), ha="center")

# ===== 6. 饼图 =====
plt.figure()   # 再建一个新图
product_sum["金额"].plot(kind="pie", autopct="%.1f%%")
plt.title("各产品金额占比")
plt.ylabel("")

plt.show()  # 一次显示所有图


# ===== 7. 按月统计销量 =====
df_clean["月份"] = df_clean["日期"].dt.month
monthly = df_clean.groupby("月份")["销量"].sum()
print(f"\n每月总销量:\n{monthly}")

# ===== 8. 画折线图（每天销量变化）=====
plt.figure()
df_clean.plot(x="日期", y="销量", kind="line", marker="o", linestyle="-", alpha=0.7)
plt.title("每日销量趋势")
plt.ylabel("销量")
plt.grid(True)
plt.show()

# ===== 9. 各产品按月的销量 =====
product_month = df_clean.groupby(["月份", "产品"])["销量"].sum().unstack()
print(f"\n各产品每月销量:\n{product_month}")

# 画分组柱状图
plt.figure()
product_month.plot(kind="bar")
plt.title("各产品每月销量对比")
plt.ylabel("销量")
plt.legend(title="产品")
plt.show()
