__author__ = 'ganeshchand'


def main():
    try:
        result = 100 / 2  # gives 50.0 Note: if you want only integer part, you can use // operator
        print('{} :{}'.format("Result", result))

    except ZeroDivisionError:

        print("You cannot divide by Zero")

if __name__ == '__main__':
    main()
