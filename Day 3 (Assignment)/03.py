"""""

Write a function that prints the digits of a number, . 
For eg: , there are 3 digits in it 3, 1 and 2 & we need to print them. 
 
[Hint - The right most digit of a number N is N%10. 
And to remove the right most digit from a number, we can do N = N / 10.] 

"""

def print_digits(number):
    if number == 0:
        print(0)
        return
    digits = []
    while number > 0:
        digit = number % 10
        digits.append(digit)
        number = number // 10
    for digit in reversed(digits):
        print(digit)

a = int(input("enter the number : "))

print_digits(a)