# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

# Examples:

# s = "leetcode"
# return 0.

# s = "loveleetcode",
# return 2.
# Note: You may assume the string contain only lowercase letters.

def solution(s):
    if len(s) == 1:
        return 0
    alphabet = {}
    for x in range(len(s)):
        if s[x] not in alphabet:
            alphabet[s[x]] = True
        else:
            alphabet[s[x]] = False
    for x in range(len(s)):
        if alphabet[s[x]] == True:
            return x
    return -1
if __name__ == '__main__':
    print(solution('hello'))
    print(solution('leetcode'))
    print(solution('loveleetcode'))

# Time complexity worst case = O(2n)
# Space complexity O(n)