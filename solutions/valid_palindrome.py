def solution(s):
    valid = "abcdefghijklmnopqrstuvwxyz1234567890"
    start = 0
    end = len(s)-1
    s = s.lower()
    stop = False
    while start < end:
        while s[start] not in valid:
            start += 1
            if start >= end:
                stop = True
                break
        while s[end] not in valid:
            end -= 1
            if end <= start:
                stop = True
                break
        if stop == True:
            break
        elif s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True
if __name__ == '__main__':
    print(solution(('.,')))
    print(solution(('help')))
    print(solution(('')))
    print(solution(('a')))
    print(solution(('....*')))
    print(solution(('race,car')))
    print(solution(('help')))

#time complexity: O(n)
#space complexity: O(1)?