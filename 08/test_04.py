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

    def runMultiple(self, mileageList):
        print("before")
        print(self.mileage)
        for idx in range(len(mileageList)):
            self.run(mileageList[idx])
        print("after")
        print(self.mileage)

# entry point
if __name__ == "__main__":
    # class / object instance
    brand = "Toyota"
    car1 = Vehicle(brand)

    car1.runMultiple([10, 20, 30, 100])

    car1.runMultiple([5000, 2000])

    car1.runMultiple([-7160])
