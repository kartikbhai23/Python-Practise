# Day 15: Exception handling
# try, except blocks to stop code from crashing on errors

# division error check
try:
    numerator = 10
    denominator = 0
    result = numerator / denominator
except ZeroDivisionError as error:
    print("Error:", error)
finally:
    print("Done checking division.")

# test conversion code without crashing
print("Mocking divide_user_inputs:")
try:
    num1 = int("10")
    num2 = int("5")
    print(f"10 / 5 = {num1/num2}")
except (ValueError, ZeroDivisionError) as e:
    print("Caught error:", e)

# exercise 1: raising errors manually
def check_age(age):
    if age < 0:
        raise ValueError("Age can't be negative!")
    return f"Age: {age}"

try:
    check_age(-5)
except ValueError as e:
    print("Error caught:", e)

# challenge: safe conversion helper
def safe_float_convert(val_str):
    try:
        return float(val_str)
    except (ValueError, TypeError):
        return 0.0

print("Float converts:", safe_float_convert("3.14"))
print("Float conversion fail test:", safe_float_convert("abc"))
print("Float None check:", safe_float_convert(None))
