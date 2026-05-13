# from pathlib import Path

# p = Path(".")
# print("当前目录：",p.resolve())

# for f in p.iterdir():
#     if f.suffix == ".py":
#         print(f"文件:{f.name} 大小:{f.stat().st_size}字节")


# from datetime import datetime,timedelta

# now = datetime.now()
# print("当前时间:",now)

# print(f"年{now.year}")
# print(f"月{now.month}")
# print(f"日{now.day}")
# print(f"时{now.hour}")

# print(f"格式化:{now.strftime('%Y-%m-%d %H:%M:%S')}")

# tomorrow = now + timedelta(days=1)
# print("明天的时间:",tomorrow.strftime('%Y-%m-%d %H:%M:%S'))

# sometime = now + timedelta(hours=-5)
# print(f"五小时前:{sometime.strftime('%Y-%m-%d %H:%M:%S')}")

# print(f"现在时间:{now.strftime('%Y-%m-%d %H:%M:%S')}")


# import random 
# print(f"随机数:{random.random():.8f}")
# print(f"随机数:{random.randint(1,100)}")
# fruits = ["苹果","香蕉","橘子","葡萄 "]
# print(f"随机选中的水果:{random.choice(fruits)}")

# random.shuffle(fruits)
# print(f"打乱顺序后的水果列表:{fruits}")

# import re
# text = "我的电话是123456789101，你的电话是987654321012"

# phonoes = re.findall(r"\d{11}",text)
# print(f"找到的电话号码:{phonoes}")

# hidden = re.sub(r"\d{11}","********",text)
# print(f"隐藏电话号码后的文本:{hidden}")


# hidden1 = re.sub(r"(\d{3})\d{4}(\d{4})",r"\1****\2",text)
# print(f"隐藏电话号码（中间4位变星号）:{hidden1}")

# # ----- 正确写法 -----
# hidden2 = re.sub(r"(\d{3})\d{4}(\d{4})", r"\1****\2", text)
# print(f"正确隐藏（中间4位变星号）:{hidden2}")


