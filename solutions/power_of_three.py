"""
Given an integer, write a function to determine if it is a power of three.

Follow up:
Could you do it without using any loop / recursion?

Credits:
Special thanks to @dietpepsi for adding this problem and creating all test cases.

3^n

1 = 1
3 = 11
9 = 1001
27 = 11001
81 = 1010001



"""


def is_power_of_three(n): 
    if n <= 0:
        return False
    return 1162261467 % n == 0
if __name__ == '__main__':
    print(is_power_of_three(3))