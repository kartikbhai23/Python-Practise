# Day 2: Basic data types
# Checking out integers, floats, strings, and booleans.

num1 = 42
num2 = 3.14159
text = "Python is fun!"
flag = False

# checking types using type() function
print(num1, "is", type(num1))
print(num2, "is", type(num2))
print(text, "is", type(text))
print(flag, "is", type(flag))

# typecasting - converting float to int chops off the decimal part
float_num = 9.99
int_num = int(float_num)
print("9.99 converted to int:", int_num)

# string to int conversion, otherwise math won't work
number_str = "150"
converted_int = int(number_str)
print("adding 50 to it:", converted_int + 50)

# exercise 1: int to float
val = 5
f_val = float(val)
print("f_val is:", f_val, "Type:", type(f_val))

# exercise 2: adding a string and string number
result = str(10) + "20"
print("Result of concatenation:", result)

# challenge: converting fahrenheit to celsius
# formula is (F - 32) * 5/9
temp_f = 98.6
temp_c = (temp_f - 32) * 5 / 9
print("Fahrenheit:", temp_f, "in Celsius is:", temp_c)
