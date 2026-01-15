# Day 5: Conditionals
# figuring out if-elif-else statements

age = 18

# check category based on age
if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
else:
    print("Adult")

# checking nested ifs
has_ticket = True
has_id = False

if has_ticket:
    if has_id:
        print("Welcome to the show!")
    else:
        print("Need ID card.")
else:
    print("No ticket.")

# exercise 1: check sign of number
number = -7.5
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

# exercise 2: leap year calculation
year = 2024
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is leap year")
else:
    print(f"{year} is not leap year")

# challenge: grading student marks
marks = 85
if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
elif marks >= 60:
    grade = "D"
else:
    grade = "F"
print(f"Marks: {marks}, Grade: {grade}")
