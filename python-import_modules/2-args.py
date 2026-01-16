#!/usr/bin/python3
import sys

if __name__ == "__main__":
    numbArg = len(sys.argv) - 1

    if numbArg == 0:
        print("0 arguments.")
    elif numbArg == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(numbArg))

    for i, arg in enumerate(sys.argv[1:], start=1):
        print("{}: {}".format(i, arg))
