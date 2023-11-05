#!/usr/bin/env python3

# write a function which takes one input
# which is assumed to a postive integer
# return True if this is even
# return False if this is odd

# example: input = 3, return Flase
# example: input = 10, return True

# hint: a = 3 % 2, a --> 1
# a = 6 % 2, a --> 0

def fun(num):
    remainder = num % 2
    if remainder == 0:
        return True
    elif remainder == 1:
        return False


# entry point
if __name__ == "__main__":
    a = 3
    print(fun(a))

    b = 10
    print(fun(b))
