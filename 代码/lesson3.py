# def great(name):
#     print(f"hello,{name}")

# great("zhangsan")
# great("lisi")


# def add(x,y):
#     return x+y  

# result = add(3,5)
# print(result)
# print(add(10,20))


# def info(name,age,city):
#     print(f"name:{name},age:{age},city:{city}")

# info("zhangsan",20,"beijing")
# info(age=30,name="lisi",city="shanghai")


# x = 10
# def test():
#     y = 20
#     print(x)
#     print(y)
# test()

# def test2():
#     # print(y)
#     print(x)
# test2()

# some = lambda x : x ** 2
# print(some(5))

# nums = [1,2,3,4,5]
# somes = list(map(lambda x : x**2 ,nums))
# print(somes)

# so = list(filter(lambda x : x % 2 == 0,nums))
# print(so)

# class dog:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def bark(self):
#         print(f"{self.name} says wangwang")

# my_dog = dog("xiaohuang",3)
# print(my_dog.name)
# print(my_dog.age)
# my_dog.bark()   


# class Student:
#     def __init__(self,name,age,score):
#         self.name = name
#         self.age = age
#         self.score = score

#     def info(self):
#         print(f"name:{self.name},age:{self.age},score:{self.score}")
# s1 = Student("zhangsan",20,90)
# s2 = Student("lisi",22,85)       
# s1.info()
# s2.info()


# class Animal:
#     def __init__(self,name):
#         self.name = name
        
#     def eat(self):
#         print(f"{self.name} 发出声音")
# class Dog(Animal):
#     def eat(self):
#         print(f"{self.name} 啃骨头")
# class Cat(Animal):
#     def eat(self):
#         print(f"{self.name} 吃鱼")


# dog =Dog("小黄 ")
# cat = Cat("小花")

# dog.eat()
# cat.eat()


# try:
#     name = input("请输入你的名字：")
#     age = int(input("请输入你的年龄："))
#     result = 100 / age
#     print(f"你好，{name}！你的年龄是{result}岁")
# except ValueError:
#     print("请输入一个有效的数字作为年龄！")
# except ZeroDivisionError:
#     print("年龄不能为零！")
# except Exception as e:
#     print(f"发生了一个错误：{e}")
# finally:
#     print("程序执行结束。")

# with open("test.txt","w",encoding="utf-8") as f:
#     f.write("这是一个测试文件。")

# with open("test.txt","r",encoding="utf-8") as f:
#     content = f.read()
#     print(content)
    

import csv
import json

with open("students.csv","w",newline="",encoding = "utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["name","age","score"])
    writer.writerow(["zhangsan",20,90])
    writer.writerow(["lisi",22,85])

with open("students.csv","r",encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

data = {"name":"zhangsan","age":20,"score":[90,85,88]}
with open("data.json","w",encoding="utf-8") as f:
    json.dump(data,f,ensure_ascii=False,indent=4)

with open("data.json","r",encoding="utf-8") as f:
    loaded = json.load(f)
    print(loaded["name"],loaded["age"],loaded["score"])