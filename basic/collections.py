__author__ = 'ganeshchand'

def main():

    # tuples in Python are immutable. You cannot add or remove
    mytuple = (1, 2, 3, 4, 4)

    print(type(mytuple), mytuple)
    print("4 occurs : {}".format(mytuple.count(4)) + " times")
    print("There are total of {}".format(mytuple.__len__()) + " values")

    #iterating

    for n in mytuple:
        print(n)

    myset = {1, 2, 3, 4}
    myset.add(5)
    myset.remove(1)
    print(type(myset), myset)
    print("There are total of {}".format(myset.__len__()) + " values")

    # lists are mutable
    mylist = [1, 2, 3, 4]
    mylist.append(5)
    mylist.insert(0, 0)
    print(type(mylist), mylist)
    print("There are total of {}".format(mylist.__len__()) + " values")
    print("Printing in Reverse")
    mylist.reverse()
    print(mylist)

    # dictionaries in Python..Similar to HashTable

    my_dictionary = { 'one': 1, 'two': 2, 'three': 3}
    print(type(my_dictionary), my_dictionary) # prints my_dictionary object

    for k in my_dictionary:  # for each key in my dictionary
        print(k, my_dictionary[k])  # print keys and values of(key)

    # alternate way to define dictionary : this is more easier and efficient way
    my_dictionary = dict(
        one=1,
        two=2,
        three=3,
        four=4,
        five='five'
    )

    #prints keys in random order
    for key in my_dictionary:
        print(key)
    # adding new key-vaue in existing dictionary
    my_dictionary['six'] = 6

    #prints kyes in sorted order
    print("sorted dictionary in alphabetical order of key")
    for key in sorted(my_dictionary.keys()):
        print(key, my_dictionary[key])

    print(my_dictionary.get('one'))


if __name__ == '__main__':
    main()