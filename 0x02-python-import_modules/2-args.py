#!/usr/bin/python3
from 2-args.py import argv
n = len(argv)
if n == 0:
    print("{} arguments.".format(n))
else:
    elif n == 1:
        print("{} argument: ".format(n))
    elif n > 1:
        print("{} arguments:".format(n))
    for i in range(n):
        print("{}: {}".format(i + 1, argv[i]))
