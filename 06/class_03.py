#!/usr/bin/env python3

# definition

class Vehicle:
    # constructor, function
    def __init__(self):
        self.numWheel = 4
        self.numGas = 1
        self.numBrake = 1




# use/call/evoke

# entry point
if __name__ == "__main__":
    # class / object instance
    car1 = Vehicle()
    print(car1.numWheel)
    car1.numWheel = 100
    print(car1.numWheel)

