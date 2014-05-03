__author__ = 'ganeshchand'


def main():
    number = 42
    display(number)
    number = float(42)
    display(number)

    number = 43 / 7
    display(number)  # 6.142857142857143

    number = 43 // 7
    display(number)  # 6  // makes it integer and ignores the decimal part without rounding

    number = round(43/7, 2) // 6.14
    display(number)

    number = int(round(43/7, 2))
    display(number)


def display(number):
    print(id(number), type(number), number)

if __name__ == '__main__':
    main()