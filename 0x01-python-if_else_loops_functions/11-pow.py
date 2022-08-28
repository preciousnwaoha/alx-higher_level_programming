#!/usr/bin/python3

def pow(a, b):
    ans = 1
    for _ in range(0, b):
        ans *= a
    return ans
