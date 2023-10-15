#!/usr/bin/env python3

# definition

class Person():
    def __init__(self, name, age, ID):
        self.name = name
        self.age = age
        self.IDstring = ID



# use/call/evoke

# entry point
if __name__ == "__main__":
    person1 = Person("Job", 25, "45g6x")
    print(person1.IDstring)

    name = "Jacob"
    age2 = 47
    ID = "s34"

    person2 = Person(name, age2, ID)
    print(person2.IDstring)
