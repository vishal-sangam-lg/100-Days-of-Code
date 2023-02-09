# Unlimited positional arguments stored as tuple
def add(*args):
    # print(args)
    ans = 0
    for n in args:
        ans += n
    return ans


print(add(3, 5, 6, 1))


# Unlimited keyword arguments stored as dictionary
def calculate(n, **kwargs):
    # print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        # self.make = kw["make"]
        # self.model = kw["model"]
        # .get will return None instead of throwing error if argument not defined
        self.make = kw.get("make")
        self.model = kw.get("model")


my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)
