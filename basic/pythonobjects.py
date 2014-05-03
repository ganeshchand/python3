__author__ = 'ganeshchand'

# everything in Python is an Object e.g. variables, functions and even code
# Every object has an ID, Type and Value
# ID uniquely identifies a particular instance of an object
# Type and ID cannot change the value during the life time of the object
# Values: Mutable objects can change, immutable objects cannot
# most fundamentals types in Python are immutable - numbers, strings, tuples
# mutable objects include lists, dictionaries, etc.

# use id(variable) to get id
# use type(variable) to to type
# use print(variable) to get value

class Animal:
    def __init__(self, kind="dog"):  # constructor can take default values. in this case,
    # kind variable has a default value of dog
        self.kind = kind;

    def animaltype(self):
        return self.kind


def main():
    animal1 = Animal()  # create an object of class Animal
    animal2 = Animal('cat')

    print(animal1.animaltype())
    print(animal2.animaltype())


if __name__ == '__main__':
    main()