#!/usr/bin/python3
if __name__ == "__main__":
    """Print the njumber of and list of arguments."""
    import sys

    n = len(sys.argv)
    if n == 0:
        print("0 arguments.")
    else:
        elif n == 1:
            print("{} argument: ".format(n))
        elif n > 1:
            print("{} arguments:".format(n))
        for i in range(n):
            print("{}: {}".format(i + 1, sys.argv[i]))
