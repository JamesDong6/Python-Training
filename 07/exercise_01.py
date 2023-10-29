#!/usr/bin/env python3

# write a function which takes three inputs (all are float)
# compare and find which number is the smallest, return and print it

def compare2_small(num1, num2):
    if num1 <= num2:
        return num1
    else:
        return num2

def compare(num1, num2, num3):
    small = compare2_small(num1, num2)
    smallest = compare2_small(small, num3)
    return smallest

# entry point
if __name__ == "__main__":
    a = 10
    b = -10
    c = 3

    re = compare(a, b, c)
    print(re)

    print(compare(a, c, b))
    print(compare(c, a, b))
