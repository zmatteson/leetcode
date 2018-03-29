"""
Fizz Buzz
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

Example:

n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
"""

def fizzbuzz(n):
    for num in range(1,n+1):
        if num % 3 == 0:
            print('Fizz',end='')
        if num % 5 == 0:
            print('Buzz', end='')
        elif num % 3 != 0 and num % 5 != 0:
            print(num,end='')
        print()

if __name__ == '__main__':
    fizzbuzz(15)