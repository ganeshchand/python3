__author__ = 'ganeshchand'

# white spaces are very important and have meanings in python


def main():
    print("White spaces are important in python")  # contains 4 spaces - which is by default for a block of code

  #print("this is another line") # contains 3 spaces...which give error
print("this is outside the main program")  # this doesn't belong as part of the main as it is same level as main()

if __name__ == "__main__":
    main()


#in this program, main() gets called at the end, so, anything outside the main() body gets executed first.