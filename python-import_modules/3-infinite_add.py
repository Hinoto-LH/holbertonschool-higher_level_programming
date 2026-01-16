#!/usr/bin/python
import sys

if __name__ == "__main__":
    numbArg = len(sys.argv) - 1
    result = 0
    for arg in (sys.argv[1:]):
        result = int(arg) + result
    print("{}".format(result))
