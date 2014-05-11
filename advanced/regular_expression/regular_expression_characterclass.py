__author__ = 'ganeshchand'

import re

# \d : digit character class : matches on [0123456789]
# \w : word character class  : matches on [a-zA-Z0-9_]
# \s : space character class : matches on [\t \n] : \t : tab and \n : new line


# custom character class: you can customize the character class. e.g
  # [a-z] instead of saying \w
  # [a-zA-Z] instead of saying \w
  # [12345] instead of saying \d

# inverse character class:
  # \D : Not a digit
  # \W : Not a word
  # \S : Not a space

# negative character class:
  # non-letter: [^a-zA-Z]. Note: if the ^ is outside the [], it will interpret it as anchor. i.e. beginning with [a-zA-Z]


def match(mypattern, mystring):
    re.escape
    if re.search(mypattern, mystring):
        print("%s matched %s" % (mypattern, mystring))

    else:
        print("%s did not match %s" % (mypattern, mystring))



mystring = "hello, 54 world"
mypatterns = ["[1-5] world", "[1-5][6-8]", "\d", "\d\d\s", "^[a-z]*,", "\D"]
for pattern in mypatterns:
    match(pattern, mystring)
