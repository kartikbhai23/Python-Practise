# Day 9: Recursion basics
# a function calling itself. need to make sure base case is correct

# simple countdown
def countdown(n):
    if n <= 0:
        print("Blastoff!")
    else:
        print(n, end=" ")
        countdown(n - 1)

print("Recursive countdown:")
countdown(5)

# factorial calculator
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial of 5 is:", factorial(5))

# exercise 1: sum up to n recursively
def recursive_sum(n):
    if n <= 1:
        return n
    return n + recursive_sum(n - 1)

print("Sum of 10:", recursive_sum(10))

# challenge: fibonacci sequence
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# print first 8 terms
print("Fibonacci terms:")
for idx in range(8):
    print(fibonacci(idx), end=" ")
print()
