#!/usr/bin/env python3

# definition
class Vehicle:
    numWheel = 4
    numGas = 1
    numBrake = 1

    # constructor, function
    def __init__(self, brand):
        self.brand = brand
        self.mileage = 0.0
    
    def run(self, mileage):
        self.mileage = self.mileage + mileage

# entry point
if __name__ == "__main__":
    # class / object instance
    brand = "Toyota"
    car1 = Vehicle(brand)

    print(car1.mileage)

    car1.run(100)
    print(car1.mileage)

    car1.run(1000)
    print(car1.mileage)

    brand = "Ford"
    car2 = Vehicle(brand)
    print(car2.mileage)
