__author__ = 'ganeshchand'

nonunicodeString = 'A unicode \u018e string \xf1'
unicodeString = u'A unicode \u018e string \xf1'

print(nonunicodeString)
print(unicodeString)
print(unicodeString.encode('utf-8')) # To convert a unicode string to bytes with an encoding such as 'utf-8'

s = '\000'
print(s)
#t = str(s,'utf-8')
t = s.encode( 'utf-8')
print('t %s' % t)

asiancharacters = u"\u5f15\u8d77\u7684\u6216"
print(asiancharacters)

print(asiancharacters.encode('utf-8'))
bytes = asiancharacters.encode('utf-8')
print(bytes.decode('utf-8'))


