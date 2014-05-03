__author__ = 'ganeshchand'

# function to generate range of numbers


def main():
    generatenumber()
    generatenumbercustom(5)


def generatenumber():
    for i in range(10):  # range function by default starts with 0 and is optional. it will stop at 9
        print(i, end='  ')  # with end= '    ', it will print the numbers in the new line
    print()  # prints new line


def generatenumbercustom(a):
    for i in range(a, 10):
        print(i, end='  ')  # prints 5, 6, 7, 8, and 9

if __name__ == '__main__':
    main()