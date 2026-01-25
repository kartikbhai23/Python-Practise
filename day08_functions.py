# Day 8: Functions
# making reusable code blocks using 'def' keyword

# first simple function
def greet():
    print("Welcome to Day 8!")

greet()

# sum function
def add_numbers(num1, num2):
    return num1 + num2

result = add_numbers(12.5, 7.5)
print("Sum is:", result)

# function with default argument
def greet_user(name="Guest"):
    print(f"Hello, {name}!")

greet_user("Kartik")
greet_user()

# exercise 1: check if number is even
def is_even(num):
    return num % 2 == 0

print("Is 10 even?", is_even(10))
print("Is 15 even?", is_even(15))

# exercise 2: max of 3 numbers
def find_max(a, b, c):
    max_val = a
    if b > max_val:
        max_val = b
    if c > max_val:
        max_val = c
    return max_val

print("Max is:", find_max(5, 12, 9))

# challenge: temperature conversion helper
def convert_temp(temp, unit="C"):
    if unit.upper() == "C":
        return (temp * 9/5) + 32
    elif unit.upper() == "F":
        return (temp - 32) * 5/9
    else:
        return "Invalid unit"

print("30C to F:", convert_temp(30, "C"))
print("86F to C:", convert_temp(86, "F"))
