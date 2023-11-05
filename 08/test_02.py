#!/usr/bin/env python3

# write a function which takes one input
# which is assumed to a postive integer
# return the factorial of this positive integer

# example: input = 3, return 3! = 3 * 2 * 1
# example: input = 10, return 10! = 10 * 9 * 8 * 7 * ... * 1
def fun(n):
    list1 = list(range(n+1))
    length = len(list1) - 2
    multiply = list1[1]
    for idx in range(length):
        multiply  = multiply * list1[idx+1]
    return multiply

def fun2(n):
    num = 1
    result = num
    while num <= n:
        result = result * num
        num = num + 1
    return result


# entry point
if __name__ == "__main__":
    a = 5
    print(fun2(a))

