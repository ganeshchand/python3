__author__ = 'ganeshchand'

# implemented using re module in Python

# Meta Characters: . ^ $ * + ? { } [ ] \ | ( )
#   . any character (single dot means any single character
#   \w word character
#   \d digit
#   \s white space  \S any non-white spaces
#   + one or more
#   * zero or more
#
#
#
#
#
#

import re


def main():
    string = r'identifier id identifies ids'
    find('id', string)  # returns id
    find('id.', string)  # returns id



def find(pattern, string):

    match = re.search(pattern, string)
    if match:
        print(match.group())
    else:
        print("Not found")

if __name__ == '__main__':
    main()



