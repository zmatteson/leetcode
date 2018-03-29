"""
Count Primes
Description:

Count the number of prime numbers less than a non-negative number, n.

Credits:
Special thanks to @mithmatt for adding this problem and creating all test cases.
"""


def countPrimes(n):
    """
    :type n: int
    :rtype: int
    """
    if n <= 2:
        return 0
    primes = [True] * (n) 
    primes[0] = primes[1] = False

    for i in range(2, n):
        if primes[i]:
            for j in range(i*i, n, i):
                primes[j] = False
    return sum(primes)


if __name__ == '__main__':
    print(countPrimes(5))
