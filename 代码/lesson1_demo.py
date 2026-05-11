# name  = input("what is your name?")
# print(f"hello,my name is {name}") 


shuiguo = ["apple","banana","orange","watermelon"]
print(f"原始列表:{shuiguo}")


shuiguo.append("grape")
print(f"添加葡萄后:{shuiguo}")

shuiguo.insert(1,"water")
print(f"在索引1处插入water后:{shuiguo}")

shuiguo.pop()
print(f"删除最后一个元素后:{shuiguo}")

shuiguo.pop(1)
print(f"删除索引1处的元素后:{shuiguo}")

print(f"前俩个是：{shuiguo[:2]}")
print(f"后俩个是：{shuiguo[2:]}")


print(shuiguo)
print(f"列表的长度为：{len(shuiguo)}")


a = [x * 2 for x in range(10)]
print(f"x * 2 ={a}" )

b = [x * 2 for x in range(10) if x % 2 == 0]
print(f"偶数 * 2 = {b}")

c = [x ** 2 for x in range(10)]
print(f"1 - 10的平方 = {c}  ")


names = ["huaduo","tangwang","niubi"]
d = [f"你好,{name}" for name in names]
print("打招呼:",d)


#11 课
print("\n ===字典操作===")
students = [
    {"name": "huaduo", "age": 18, "append": "python"},
    {"name": "zhangsan", "age": 20, "append": "java"},
]
print(f"原始字典列表:{students}")   

students[0]["city"] = "beijing"
print(f"在第一个字典中添加city键后:{students}")

print(f"name is :{students[0].get("name")}")
print(f"iphone is :{students[0].get("iphone","没有这个键")}")

for key,value in students[0].items():
    print(f"{key}:{value}")
for key,value in students[1].items():
    print(f"{key}:{value}")

scores = {"huaduo": 90, "zhangsan": 85}
for name,score in scores.items():
    print(f"{name}的分数是{score}")

total = sum(scores.values())
avg = total / len(scores)
print(f"总分:{total}")
print(f"平均分:{avg}")

print(f"平均分为:{avg:.2f}")

a = {x for x in range(10)}
b = {x for x in range(10,20)}
print(f"集合a:{a}")
print(f"集合b:{b}   ")


a.add(12)
print(f"添加12后集合a:{a}")
a.remove(5)
print(f"删除5后集合a:{a}")

print(f"集合a和b的交集:{a&b}")
print(f"集合a和b的并集:{a|b}")
print(f"集合a和b的差集:{a-b}")


t = tuple(x for x in range(5))
lst  =  [ x for x in range(5)]

print(f"元组t:{t}")
print(f"列表lst:{lst}")

lst[1] = 20
print(f"修改lst后:{lst}")

point  = (100,200)
print(f"点的坐标为：{point}")