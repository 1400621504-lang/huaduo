class Macbook:
    cpu = "m1"
    gpu = "m1"
    neicun = "16g"
    rate = 0.85


    def __init__(self, name,color,price,cpu):
        self.name = name
        self.color = color
        self.price = price
        self.cpu = cpu

mac = Macbook("m1pro","blue",100,"m1max")
print(mac.name)
print(mac.color)
print(mac.price)

print(mac.rate)
print(mac.gpu)
print(mac.cpu)