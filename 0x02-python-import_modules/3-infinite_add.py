#!/usr/bin/python3
import argv
sum = 0
for n in range(len(argv)):
    sum += int(argv[n])
print("{}".format(sum))

