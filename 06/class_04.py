#!/usr/bin/env python3

# definition

class Vehicle:
    # constructor, function
    def __init__(self, brand):
        self.numWheel = 4
        self.numGas = 1
        self.numBrake = 1
        self.brand = brand




# use/call/evoke

# entry point
if __name__ == "__main__":
    # class / object instance
    brand = "toyota"
    car1 = Vehicle(brand)
    print(car1.brand)
    car1.brand = 100
    print(car1.brand)

