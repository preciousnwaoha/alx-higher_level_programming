#!/usr/bin/python3
if __name__ == "__main__":
    """Print addition of all arguments."""
    import sys

    sum = 0
    for n in range(len(sys.argv)):
        sum += int(sys.argv[n])
    print("{}".format(sum))

