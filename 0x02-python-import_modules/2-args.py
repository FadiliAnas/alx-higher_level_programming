#!/usr/bin/python3
import sys

if __name__ == "__main__":
    i = 0;
    if(len(sys.argv)-1) != 0:
        print("{} arguments:".format(len(sys.argv)-1))
        while i + 1 < len(sys.argv):
            print("{}: {}".format(i+1,sys.argv[i + 1]))
            i = i + 1
    else:
        print("{} arguments.".format(len(sys.argv)-1))

