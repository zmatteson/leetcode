"""
Number of 1 Bits
Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).

For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011, so the function should return 3.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.
"""


def hammingWeight(n):
    """
    :type n: int
    :rtype: int
    """
    weight = 0
    while n:
        weight += 1 & n
        n = n >> 1
    return weight

if __name__ == '__main__':
    print(hammingWeight(2))
    print(hammingWeight(1))
    print(hammingWeight(9))