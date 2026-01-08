# Day 3: Input and Output
# Learning print formatting and user input.

# note: input() always returns a string, need to convert if using numbers
# using a default value for automated testing so it doesn't freeze
user_name = "Kartik" 
print("Hello, " + user_name + "! Welcome to Python.")

# birth year conversion
age_input = "2006"
birth_year = int(age_input)
current_year = 2026
age = current_year - birth_year
print("You are approximately", age, "years old.")

# f-strings are so clean! much better than using commas
print(f"User {user_name} is {age} years old.")

# exercise 1: add two numbers
num_a = 15.0
num_b = 30.5
sum_res = num_a + num_b
print(f"Sum: {sum_res}")

# challenge: calculate body mass index (BMI)
# weight / (height squared)
weight = 72.0
height = 1.75
bmi = weight / (height ** 2)
print(f"Your calculated BMI is: {bmi:.2f}")
