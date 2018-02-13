def myAtoi(s):
    isNeg = False
    for char in s:
        if char == " ":
            s = s[1:]
        else:
            break
    if s[0] == '-':
        isNeg = True
        s = s[1:]
    ans = ''
    while s[0].isdecimal:
        ans = ans + s[0]
        s = s[1:0]
        if len(s) == 0:
            break
    try:
        if isNeg == True:
            return -1*int(ans)
        else: 
            return int(ans)
    except ValueError:
        return 0
if __name__ == '__main__':
    print(myAtoi('!!'))
    print(myAtoi('1'))
    print(myAtoi('         1'))
    print(myAtoi('-1.1.1'))