#!/usr/bin/python
if __name__ == "__main__":
    import sys
    numbArg = len(sys.argv) - 1
    result = 0
    for arg in (sys.argv[1:]):
        result = int(arg) + result
    print("{}".format(result))
