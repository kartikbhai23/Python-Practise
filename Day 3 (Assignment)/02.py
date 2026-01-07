#. Write a function that takes two integers and and prints all even  numbers between them (inclusive)

def print_even_numbers(start, end):
    for num in range(start, end + 1):
        if num % 2 == 0:
            print(num)

a = int(input("enter the 1st number: "))
b = int(input("enter the 2nd number: "))

print_even_numbers(a, b)