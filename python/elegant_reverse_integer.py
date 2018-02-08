'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:
Input: 123
Output:  321

Example 2:
Input: -123
Output: -321

Example 3:
Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only hold integers within the
32-bit signed integer range. For the purpose of this problem, assume that your function 
returns 0 when the reversed integer overflows.
'''
def solution(x):
    '''
    :type x: int
    :rtype: int
    '''
    isNeg = False
    if x < 0:
        isNeg = True
        x *= -1
    ans = 0
    while x > 0:
        ans*=10
        integer = (x%10)
        ans += integer
        x //= 10     
    if ans > (2**31)-1:
        return 0
    elif isNeg:
        return ans*-1
    else:
        return ans
if __name__ == '__main__':
    print(solution(123))
    print(solution(-123))
    print(solution(120))

#My code feels fancier because I use modulo and divion to strip the digits, but I'm
#not sure that the real improvement in performance would be here.  I'm calling it 
#the "elegant" solution - but it could be improved.