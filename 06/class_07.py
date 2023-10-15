#!/usr/bin/env python3

# definition

class Vehicle:
    whetherNew: bool
    a: float

    # constructor, function
    def __init__(self, brand):
        self.numWheel = 4
        self.numGas = 1
        self.numBrake = 1
        self.brand = brand
        self.mileage = 0

    def run(self, mileage):
        # a += b      <=>   a = a + b
        print("Before ", self.mileage)
        self.mileage += mileage
        print("After ", self.mileage)

    def squre(self, num):
        return num ** 2

    def run2(self, mileage):
        print("Before ", self.mileage)
        res = self.squre(mileage)
        self.mileage += res
        print("After ", self.mileage)


# use/call/evoke

# entry point
if __name__ == "__main__":
    # class / object instance
    brand1 = "toyota"
    car1 = Vehicle(brand1)

    res = car1.squre(14)
    print(res)

    car1.run2(20)

    # print(car1.whetherNew)

    car1.whetherNew = True

    print(car1.whetherNew)



