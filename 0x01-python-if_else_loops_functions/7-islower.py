#!/usr/bin/python3

def islower(c):
    """Check for lowercase in string"""
    if ord(c) in range(96, 123):
        return True
    else:
        return False
