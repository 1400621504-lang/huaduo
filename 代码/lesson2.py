# scores  = int(input("输入你的分数："))

# if scores >=90:
#     print("优秀")
# elif scores >=80:
#     print("良好")
# elif scores >=70:
#     print("中等")
# elif scores >=60:
#     print("及格")
# else:    print("不及格")    

# x = None

# if x is None:
#     print("x is None")

# if x is not None :
#     print("x is not None")

# for i in range(5):
#     print(i)

# fruits = ["苹果","蓝莓","草莓"]
# for fruit in fruits:
#     print(fruit)

# for index,f in enumerate(fruits):
#     print(index,f)


# import random

# target  = random.randint(1,100)
# guess = 0
# count = 0

# while guess is not target:
#     guess = int(input("请输入一个数字:"))
#     count += 1
#     if guess < target:
#         print("猜小了")
#     elif guess > target:
#         print("猜大了")

# print(f"恭喜你，猜对了，一共猜了{count}次")


# for i in range(1,11):
#     if i == 5:
#         break
#     else:
#         print(i)

# for i in range(1,11):
#     if i % 2 ==0:
#         print(i)
#         continue

# names = ["zhangsan","lisi","wangba"]
# ages = [21,22,23]

# for name,ages in zip(names,ages):
#     print(f"{name}的年龄是{ages}岁")



# a = [0,1]
# while len(a)<20:
#    b = a[-1] + a[-2]
#    a.append(b)
# print(a)

# for i in range(2,101):
#     s = True
#     for j in range(2,i):
#         if i % j == 0:
#             s = False
#             break
#     if s:
#         print(i)

text = "hello world hello python hello java"
words = text.split()
word = {}
for w in words:
    if w in word:
        word[w] += 1
    else:
        word[w] = 1
print(word)