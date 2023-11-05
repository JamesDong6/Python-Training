#!/usr/bin/env python3

# write a function which takes one input
# which is assumed to be a list of numbers
# return the product of all the numbers in the list

# example: li = [3, -4, 5], return 3 * (-4) * 5
# example: li = [10], return 10
# example: li = [26, -3, 10, 90], return 26 * (-3) * 10 * 90


def product2(inputList):
    length = len(inputList) - 1
    multiply = inputList[0]
    for idx in range(length):
        multiply  = multiply * inputList[idx+1]
    return multiply


# entry point
if __name__ == "__main__":
    a = [3, 4, 5, 6, 7,]
    print(product2(a))

    a = [0, -3, 4, 5]
    print(product2(a))
