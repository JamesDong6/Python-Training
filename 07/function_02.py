#!/usr/bin/env python3

# for-loop, list (array)
def fun2(inputList):
    for a1 in range(len(inputList)):
        print(inputList[a1])

def fun3(inputList):
    b = len(inputList)
    for a1 in range(b):
        print(inputList[a1])

# entry point
if __name__ == "__main__":
    li = [-3, -3, 10, 4, "John", 3.55]
    fun2(li)
