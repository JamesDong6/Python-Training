#!/usr/bin/env python3

# definition

class Vehicle:
    # constructor, function
    def __init__(self, brand):
        self.numWheel = 4
        self.numGas = 1
        self.numBrake = 1
        self.brand = brand

    def run(self):
        print(self.brand)
        print("This is run")



# use/call/evoke

# entry point
if __name__ == "__main__":
    # class / object instance
    brand1 = "toyota"
    brand2 = "ford"
    car1 = Vehicle(brand1)
    car2 = Vehicle(brand2)

    # car1.run()
    car2.run()

