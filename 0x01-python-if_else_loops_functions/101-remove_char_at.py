#!/usr/bin/bash

def remove_char_at(str, n):
    """Create a copy of the string wothout the character at index n."""
    if n < 0:
        return (str)
    return (str[:n] + str[n+1:])
