__author__ = 'ganeshchand'

import re
def regex_search(pattern_string, string_source):


    if re.search(pattern_string,string_source):
        print("%s matched %s" % (pattern_string, string_source))
    else:
        print("%s did not match %s" % (pattern_string, string_source))

# matching a pattern in one string

mystring_anchors = 'aaaaa!@#$!@#$aaaaaadefg'
pattern_withoutanchors = r'@#\$!'  # $ sign needs escaping if it doesn't represent need to represent its special meaning.
                                   #  It is an anchor reserved character - it marks the end of the string
                                   # that means, if you say aab$ , you are looking for a string that that ends with pattern aab
                                   # there should be absolutely nothing beyond aab


regex_search(pattern_withoutanchors, mystring_anchors)


pattern_withanchors = r'defg$'


regex_search(pattern_withanchors, mystring_anchors)


# patterns to be matched

patterns = ["defg$", "^d", "^a", "^a*!"]
# defg$ : string must end with defg
# ^d: must begin with d
# ^a: must begin with
# ^a*!: must beging with a followed by any number of characters and !

for patterntobematched in patterns:
    regex_search(patterntobematched, mystring_anchors)

# matching a pattern in an array of string

