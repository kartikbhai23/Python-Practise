# Day 4: Operators in Python
# practicing arithmetic and logical operators today

a = 15
b = 4
# basic math ops
print("15 / 4 =", a / b)
print("15 // 4 (floor) =", a // b)
print("15 % 4 (modulo) =", a % b)
print("2^5 =", 2 ** 5)

# logic and comparison tests
x = 10
y = 20
z = 10
print("Is x equal to z?", x == z)
print("Is x > y?", x > y)
print("logical test:", (x < y) and (y > z))
print("or test:", (x > y) or (y > z))
print("not of True:", not True)

# exercise 1: even/odd check
test_num = 17
is_even = (test_num % 2 == 0)
print(f"Is {test_num} even? {is_even}")

# exercise 2: fast assignment operators
score = 10
score += 5
score *= 2
print("Final score:", score)

# challenge: calculate simple interest
# SI = P * R * T / 100
principal = 5000
rate = 4.5
time_years = 3
interest = (principal * rate * time_years) / 100
total_amount = principal + interest
print(f"Interest: {interest}, Total to pay: {total_amount}")
