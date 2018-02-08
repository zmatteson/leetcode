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
    #inelegant solution:
    isNeg = False
    if x < 0:
        isNeg = True
        x *= -1
    ans = str(x)
    #reverse string
    ans = ans[::-1]
    if isNeg:
        ans = '-' + ans
    ans = int(ans)
    #check for overflow
    if abs(ans) > (2**31)-1:
        ans = 0
    return ans

if __name__ == '__main__':
    print(solution(123))
    print(solution(-123))
    print(solution(120))

#this is a quick hack made possible by abusing strings, but there could a more 
#elegant way to solve