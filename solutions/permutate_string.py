#1 string
#variables: length, start, stop
#how to permute string?  
#swap 2 string: 0 and 1
# swap 3: print, (end, end-1) (start and middle) 
def solution(s):
    s = list(s)
    permute(s, 0, len(s)-1)

def permute(s, l, r):
    if l == r:
        print(''.join(s))
    else:
        while(l < r):
            permute(s, l, r)
            l += 1

def swap(s, l, r):
    temp = s[l]
    s[l] = s[r]
    s[r] = temp
            
if __name__ == '__main__':
    solution('abc')




    