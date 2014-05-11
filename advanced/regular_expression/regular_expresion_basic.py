__author__ = 'ganeshchand'

import re

print("Basic Pattern Search")
mystring = 'abcdefgh'
pattern = r'de f'  # r -  means raw string it is important to use raw string

if re.search(pattern, mystring):
    print('found'+' '+pattern)
else:
    print('Not matched')

# important
# re matches will be consecutive character by character.
# re matches are on substring(unless specified otherwise...match doesn't have to be a whole..
