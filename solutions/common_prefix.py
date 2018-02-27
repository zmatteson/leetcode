def longestCommonPrefix(strs):
    min_length = find_min_length(strs)
    ans = ''
    for i in range(min_length):
        char = strs[0][i]
        for j in range(len(strs)):
            if char != strs[j][i]:
                return ans
        ans = ans + char
    return ans
            

def find_min_length(strs):
    return min(map(len, strs))

if __name__ == '__main__':
    print(longestCommonPrefix(['']))
    print(longestCommonPrefix(['a', 'b', 'c']))
    print(longestCommonPrefix(['aa','a']))
    print(longestCommonPrefix(['aa','aardvark']))