__author__ = 'ganeshchand'


def main():
    a = 10  # int
    display(a, None)
    a = 10.2  # float
    display(a, None)
    a = "Hello"  # string
    display(a, None)
    a = {1, 2, 3, 4}  # set of values
    display(a, None)
    a = [1, 2, 3, 4]  # list of values
    display(a, None)

    a = (1, 2, 3, 4) # tuples
    display(a, None)

    a, b = 1, 0
    display(a, b)


def display(a, b=None):
    if b is None:
        print(type(a), a)

    else:
        print(type(a), type(b), a, b)
        if a > b:
            print(" a greater than b")
        elif b > a:
            print("b greater than a")
        else:
            print("Both are equal")



# def display(a, b):
#     print(type(a), type(b), a, b)
#     # print("a greater than b" if a > b else "b is greater than a")


if __name__ == '__main__':
    main()
