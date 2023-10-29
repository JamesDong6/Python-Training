#!/usr/bin/env python3

# write a function which takes one input
# which is assumed to be a list of numbers
# use for loop to find out the largest number
# in the list, and return it

def compare2(num1, num2):
    if num1 >= num2:
        return num1
    else:
        return num2

def fun(inputList):
    length = len(inputList) - 1
    larger = inputList[0]
    for idx in range(length):
        larger = compare2(larger, inputList[idx+1])
    return larger


# entry point
if __name__ == "__main__":
    a = [1000, 10, -3, 100, -30, 27, 89, 150]
    print(fun(a))

    b = [15]
    print(fun(b))
