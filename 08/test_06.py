#!/usr/bin/env python3

# write a function which takes one input
# which is assumed to a list of postive integers
# print Even or Odd for every number


def fun(num):
    remainder = num % 2
    if remainder == 0:
        return True
    elif remainder == 1:
        return False
    
def main_fun(inputList):
    for idx in range(len(inputList)):
        evenFlag = fun(inputList[idx])
        if evenFlag:
            print("Even")
        else:
            print("Odd")


# entry point
if __name__ == "__main__":
    li = [3, 2, 10, 1, 7]
    main_fun(li)
