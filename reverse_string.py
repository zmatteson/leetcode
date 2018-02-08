#!/usr/bin/env python3
"""
Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".
"""
def reverseString(s):
    """
    :type s: str 
    :rtype: str
    """
    return s[-1::-1]
if __name__ == '__main__':
    s = 'hello world!'
    print(reverseString(s))
