# Given two strings s and t, write a function to determine if t is an anagram of s.

# For example,
# s = "anagram", t = "nagaram", return true.
# s = "rat", t = "car", return false.

# Note:
# You may assume the string contains only lowercase alphabets.
def solution(s,t):
    if len(s)!=len(t):
        return False
    d1 = {}
    for char in s:
        if char not in d1:
            d1[char] = 1
        else:
            d1[char] += 1
    d2 = {}
    for char in t:
        if char not in d2:
            d2[char] = 1
        else:
            d2[char] += 1
    if len(d1) != len(d2):
        return False
    for key in d1:
        if key not in d2:
            return False
        elif d2[key] != d1[key]:
            return False
    return True

if __name__ == '__main__':
    print(solution('rat','car'))
    print(solution('banana','ananab'))
    print(solution('true','truthy'))