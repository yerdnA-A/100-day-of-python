def add(*args):
    soma = sum(args)
    return soma

print(add(1,2,3))

def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)

class Car():

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model") 

my_car = Car(make='Dodge')
print(my_car.model)