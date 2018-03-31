# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

# Given two integers x and y, calculate the Hamming distance.

# Note:
# 0 ≤ x, y < 231.

def hamming_distance(a,b):
    x = a^b
    distance = 0
    while x:
        distance += 1 & x
        x = x >> 1
    return distance

if __name__ == '__main__':
    print(hamming_distance(14,3))