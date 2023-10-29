#!/usr/bin/env python3

# write a function which takes one input
# which is assumed to be a list of numbers
# return the summation of all the numbers in the list

# example: li = [3, -4, 5], return 3 + (-4) + 5
# example: li = [10], return 10
# example: li = [26, -3, 10, 90], return 26 + (-3) + 10 + 90

def summation(num1, num2):
    sum = num1 + num2
    return sum

def summation1(inputList):
    length = len(inputList) - 1
    sum = inputList[0]
    for idx in range(length):
        sum = summation(sum, inputList[idx+1])
    return sum 

def summation2(inputList):
    length = len(inputList) - 1
    sum = inputList[0]
    for idx in range(length):
        sum = sum + inputList[idx+1]
    return sum


# entry point
if __name__ == "__main__":
    a = [3, 4, 5, 6, 7,]
    print(summation1(a))

    b = [6]
    print(summation1(b))
