class Car:
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price

    def __str__(self):
        return f'{self.name}--{self.color}--{self.price}'
    def __eq__(self, other):
        return self.name == other.name and self.color == other.color and self.price == other.price
    def __lt__(self, other):
        return self.price < other.price


c1 = Car("macbook","blue", 100)
c2 = Car("macbook","blue", 100)
c3 = Car("macbook","blue", 200)
print(c1)

print(c1==c2)
print(c1!=c2)
print(c1==c3)
print(c1<c3)