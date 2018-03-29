"""
Roman to Integer
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.

I	1
V	5
X	10
L	50
C	100
D	500
M	1000

IV	4 = 5 - 1
IX	9 = 10 - 1
XL	40 = 50 - 10
XC	90 = 100 - 10
CD	400 = 500 - 100
CM	900 = 1000 - 100


"""

def roman_to_integer(r):
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C':100, 'D':500, 'M':1000}
    ans = 0
    i = len(r) -1
    while i >= 0:
        ans += roman_map[r[i]]
        if i - 1 >= 0 and roman_map[r[i]] > roman_map[r[i-1]]:
            ans -= roman_map[r[i-1]]
            i -= 1
        i -= 1
    return ans

if __name__ == '__main__':
    print(roman_to_integer('XCVI'))
    print(roman_to_integer('V'))
    print(roman_to_integer('IV'))
            
    
