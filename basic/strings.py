__author__ = 'ganeshchand'


def main():
    string = "This is a new string"
    print(string)

    string_with_escape_character = "This is a new \nline"
    print(string_with_escape_character)

    string_ignore_escapae_character = r"This ia anew \nline"  # r marks the string as raw string
    print(string_ignore_escapae_character)

    number = 1
    print("The input number is {}".format(number))  # This is a Python 3 syntax. In a string,
    # you can use {} which gets substituted by format()

    print("The input number is %s" % number)  # This i Python 2 syntax

    # to use strings that spans multiple lines. You can use both single our double quite but they need to be 3
    # \ character escapes the beginning line to be included as part of the string
    long_string = '''\
test
test
test
test
test'''
    print(long_string)


if __name__ == '__main__':
    main()
