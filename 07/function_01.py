#!/usr/bin/env python3

# definition
def compare2(num1, num2):
    if num1 >= num2:
        return num1
    else:
        return num2


# entry point
if __name__ == "__main__":
    a = 10
    b = -2
    result = compare2(a, b)
    print(result)
