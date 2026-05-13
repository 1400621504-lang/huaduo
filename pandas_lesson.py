import pandas as pd 
import matplotlib.pyplot as plt
# # data = {
# #     "name" : ["alice","mike","bob"],
# #     "age" : [25,30,35],
# #     "city" : ["new york","los angeles","chicago"]
# # }

# # df = pd.DataFrame(data)
# # print(df)


# # print(df.head(2))
# # print(df.columns.tolist())
# # print(df.shape)
# # print(df.dtypes)
# # print(df.describe())

# # df2 = pd.read_csv("students.csv")
# # print(df2)

# # # print("name:\n",df2["姓名"])

# # # print("name and age:\n",df2[["姓名","年龄"]])

# # # print(f"city:\n {df2['城市']}")

# # # high  = df2[df2["成绩"]>90 ]
# # # print(f"成绩大于90的学生：\n {high}")

# # # group = df2.groupby("城市")["成绩"].mean()
# # # print(f"按城市分组的平均成绩：\n {group}")

# # print(f'第0行:\n {df2.loc[0]}')
# # print(f'第0行:\n {df2.iloc[0]}')
# # print(f"前2行前3列:\n {df2.iloc[:2,:3]}")

# # df2.to_csv("结果.csv", index=False, encoding="utf-8")


# # df3 = pd.read_csv("脏数据.csv")

# # print(f"每列缺失数:\n{df3.isnull().sum()}")


# # df_clean = df3.dropna()
# # print(f"删除缺失值后的数据:\n{df_clean}")

# # df_fill = df3.copy()
# # df_fill["年龄"] = df_fill["年龄"].fillna(df_fill["年龄"].mean())
# # df_fill["成绩"] = df_fill["成绩"].fillna(df_fill["成绩"].mean())
# # print(f"填充缺失值后的数据:\n{df_fill}")

# # df_fill["年龄"] = df_fill["年龄"].astype(int)
# # df_fill["成绩"] = df_fill["成绩"].astype(int)
# # print(f"整理后的：\n {df_fill}")

# # grouped = df_fill.groupby("城市")["成绩"].agg(["mean","max","min","count"])
# # print(f"按城市分组统计成绩：\n{grouped}")

# # # grouped2 = df_fill.groupby("年龄")["成绩"].agg(["mean","max","min","count"])
# # # print(f"按城市分组统计成绩：\n{grouped2}")


# # df_a = pd.DataFrame({
# #     "学生ID" : [1,2,3],
# #     "城市"   : ["北京","广州","上海"],
# #     "电话" : ["138000","129000","123000"]
# # })

# # df_b = pd.DataFrame({
# #     "学生ID":[1,2,3],
# #     "姓名" : ["张三","李四","王五"],
# #     "成绩" : ["138","129","120"]

# # })

# # merged = pd.merge(df_a,df_b,on = "学生ID")
# # print(f"合并后的表:\n{merged}")

# # df_1 = pd.DataFrame({
# #     "姓名": ["张三","李四"],
# #     "成绩": [88,90]
# # })

# # df_2 = pd.DataFrame({
# #     "姓名" : ["王八","赵六"],
# #     "成绩": [99,100]
# # })

# # result = pd.concat([df_1,df_2])
# # print(f"上下合并:\n{result}")

# # sorted_df = result.sort_values("成绩",ascending=False)
# # print(f"排序后的成绩:{sorted_df}")


# df = pd.read_csv("脏数据.csv")
# print(f"原始数据:{df}")

# print(f"缺失情况:\n{df.isnull().sum()}")

# df2 = df.copy()
# df2["年龄"] = df2["年龄"].fillna(df2["年龄"].mean()).astype(int)
# df2["成绩"] = df2["成绩"].fillna(df2["成绩"].mean()).astype(int)

# # high = df2[df2["成绩"]>80]
# # print(f"成绩大于80:\n{high}")

# # grouped = df2.groupby("城市")["成绩"].agg(["mean","max","min","count"])
# # grouped["mean"] = grouped["mean"].astype(int)
# # print(f"按各个城市统计:\n{grouped}")


# # sorted = df2.sort_values("成绩",ascending= False)
# # print(f"成绩排名:\n{sorted}")

# # df.to_csv("练习结果.csv",index = False,encoding="utf-8")
# # print("已经导出 练习结果.csv")

# # def grade(score):
# #     if score >= 90 :
# #         return "优秀"
# #     elif score >= 80:
# #         return "良好"
# #     elif score >= 60:
# #         return "及格"
# #     else:
# #         return "不及格"
# # df2["评级"] = df2["成绩"].apply(grade)
# # print(df2[["姓名","成绩","评级"]])

# # pivot = pd.pivot_table(
# #     df2,
# #     index = "城市",
# #     columns = "评级",
# #     values = "姓名",
# #     aggfunc = "count",
# #     fill_value = 0,
# #     margins = True
# # )

# # print(f"各个城市评级人数:\n{pivot}")


# # ===== 销售数据透视表 =====

# sales = pd.DataFrame({
#     "销售员": ["张三", "李四", "王五", "张三", "李四", "王五", "张三", "李四"],
#     "季度":   ["Q1", "Q1", "Q1", "Q2", "Q2", "Q2", "Q3", "Q3"],
#     "产品":   ["A", "A", "B", "A", "B", "B", "B", "A"],
#     "金额":   [100, 150, 200, 130, 180, 220, 90, 160]
# })

# print("原始数据:\n", sales)

# # 透视：行=销售员，列=季度，值=销售总额
# pivot_sales = pd.pivot_table(
#     sales,
#     index="销售员",
#     columns="季度",
#     values="金额",
#     aggfunc="sum",
#     fill_value=0
# )
# print(f"\n各销售员每季度销售额:\n{pivot_sales}")

# # 透视2：行=产品，列=季度，值=销售总额
# pivot_product = pd.pivot_table(
#     sales,
#     index="产品",
#     columns="季度",
#     values="金额",
#     aggfunc="sum",
#     fill_value=0
# )
# print(f"\n各产品每季度销售额:\n{pivot_product}")

# df  = pd.DataFrame(
#     {
#         "name" : ["huaduo","tt"],
#         "age" :["23", "20"],
#         "city" : ["wuhan","wuhan"]
#     }
# )
# print(df.head(1))
# df.columns.tolist
# df.shape
# df.dtypes
# df.describe()
# print(df)

plt.rcParams["font.sans-serif"] = ["Arial Unicode MS", "SimHei", "PingFang SC"]
plt.rcParams["axes.unicode_minus"] = False
df= pd.read_csv("脏数据.csv")
df2 = df.copy()
df2["年龄"] = df2["年龄"].fillna(df2["年龄"].mean()).astype(int)
df2["成绩"] = df2["成绩"].fillna(df2["成绩"].mean()).astype(int)

# city_score = df2.groupby("城市")["成绩"].mean().astype(int)
# print(city_score)

# ax = city_score.plot(kind = "bar")
# plt.title("各城市的平均成绩")
# plt.xlabel("城市")
# plt.ylabel("平均成绩")
# for i, v in enumerate(city_score):
#     ax.text(i, v + 1, str(v), ha="center")
# plt.show()

city_count = df2["城市"].value_counts()
print(city_count)

city_count.plot(kind = "pie",autopct = "%.1f%%")
plt.title("各城市人数占比")
plt.ylabel("")
plt.show()


temps =pd.DataFrame({
    "星期": ["周一","周二","周三","周四","周五","周六","周天"],
    "气温": [22,24,23,33,34,35,35]
})

temps.plot(x = "星期", y = "气温",kind = "line", marker = "o")
plt.title("气温一周变化")
plt.ylabel("气温")
plt.show()