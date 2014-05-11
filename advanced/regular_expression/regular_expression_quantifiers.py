__author__ = 'ganeshchand'

import re
# previous examples
# r'abc'
# r'^abc'
# r'abc$'
# r'\$\d\d.\d\d' # would match on  $13.45

test_strings = ['$123778.99', '13.45', '1.45', '113.99', '1113.99', '.99']
test_patterns = ['\d\.\d\d', '\d\d\.\d\d', '\d+\.\d\d']

for mypattern in test_patterns:

    print()
    print("using pattern : %s" % mypattern)
    print()

    for mystring in test_strings:

        if re.search(mypattern, mystring):

            print("%s matches %s " % (mypattern, mystring))

        else:
            print("%s did not match %s" % (mypattern, mystring))

