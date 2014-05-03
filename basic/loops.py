__author__ = 'ganeshchand'


def main():

    # while loop
    # example is to generate simple fibonacci series - sum of 2 = 3rd
    generate_fibonacci_series(50)
    print()


    # for loop
    for i in [1, 2, 3, 4, 5]:
        print(i, end='  ')

    print()
    for c in 'python':
        print(c)

    # enumeration
    # when you want the index position when you are iterating, use enumerate function

    for index, value in enumerate('python'):
        if value == 'h':
            print('Found h at {}'.format(index))



def generate_fibonacci_series(max_number):
    a, b = 0, 1
    while b < max_number:
        print(b, end='  ')
        a, b = b, a+b

if __name__ == '__main__':
    main()