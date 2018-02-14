"""
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.
"""

def get_sequence(i):
    ans = '1'
    for x in range(1,i):
        count = 0
        l, r = 0, 0
        while (r<=len(ans)):
            if r == len(ans):
                ans = ans[:l] + str(count) + ans[l]
                break
            elif ans[l]==ans[r]:
                count += 1
                r +=1
            else:
                ans = ans[:l] + str(count) + ans[l] + ans[r:]
                r += 2 - count
                count = 0
                l = r
    return int(ans) 