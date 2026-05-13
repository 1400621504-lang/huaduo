# class Car:
#     def __init__(self,color, brand, name,price):
#         self.color = color
#         self.brand = brand
#         self.name = name
#         self.price = price
#         print("初始化完毕！")
#
#     def running(self):
#         print(f"{self.brand} {self.name} 正在高速行驶...")
#
#     def total_cost(self,discount,rate):
#         total_cost = self.price * discount * rate
#         return total_cost
#
#
# c1  = Car("red","BWM","x1",999)
#
# total = c1.total_cost(0.2,0.5)
# c1.running()
# print("提车的总费用：",total)

class Macbook:
    def __init__(self, name,color, price):
        self.name = name
        self.color = color
        self.price = price

    def start(self):
        print(f"型号是{self.name} 颜色为{self.color},价格是{self.price}")

    def mindou(self):
        print("-"* 20)

    def cost_price(self,discount,jiaoyu):
            cost_price = (self.price * discount) - jiaoyu
            return cost_price

mac = Macbook("macbook pro","break",7999)
total  =  mac.cost_price(0.85,500)
mac.start()
mac.mindou()
print(f"经过教育优惠和国补后的价格为：{total}")

