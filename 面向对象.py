class Car:
    def __init__(self, c_color,c_brand,c_price):
        self.color = c_color
        self.brand = c_brand
        self.price = c_price
        print("对象属性初始话完毕！")


c1 = Car("huaduo","baw","80w")
print(c1.__dict__)
print(c1.color)
print(c1.brand)
print(c1.price)