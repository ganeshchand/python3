__author__ = 'ganeshchand'

import os


def main():

#check if a directory exist and if it doesn't, create a directory
    directorypath = "/Users/Shared/gmcbookproroot/gh/gc/projects/python/learnpython3"

    if not os.path.exists(directorypath):
        os.makedirs(directorypath)
        print("Created directory %s" % directorypath)
    else:
        print("%s already exists" % directorypath)
        print(os.pathsep)
        print(os.pardir)
        print(os.path.getctime(directorypath))
        print(os.path.getsize(directorypath))


if __name__ == '__main__':
    main()

