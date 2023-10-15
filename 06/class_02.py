#!/usr/bin/env python3

# definition

class Vehicle:
    numWheel = 4
    numGas = 1
    numBrake = 1




# use/call/evoke

# entry point
if __name__ == "__main__":
    # class / object instance
    car1 = Vehicle()
    car2 = Vehicle()
    print(car1.numWheel)
    car1.numWheel = 100
    print(car1.numWheel)

