__author__ = 'ganeshchand'

import os


def main():
    search_directory = '/Users/ganeshchand/Downloads/lesson1/test'

    for root, dirs, files in os.walk(search_directory):
        # print(root)  # node in a tree - a node is a directory that has sub-directory or a file
        # print(dirs) # list of directories within a node
        #print(files)  # file(s) within a tree

        # to walk the directories --

        for dir in dirs:
            # print("|"+os.path.join(root, dir)+"_")
            print(root)
            # print('__'+dir)
            print('  |__'+dir)
            for file in files:
                #print("||"+os.path.join(root, file))
                print("     |__"+file)

    for root, dirs, files in os.walk(search_directory):
        root_level = root.replace(search_directory, '').count(os.sep)
        indent = ' ' * 4 * (root_level)
        print('{}{}/'.format(indent, os.path.basename(root)))
            #{} means just the next positional argument, with default format;
            #basename Returns the final component of a pathname
        subindent = (' ' * 4 * (root_level + 1))

        for f in files:
            print('{}{}'.format(subindent, f))

if __name__== '__main__':
    main()