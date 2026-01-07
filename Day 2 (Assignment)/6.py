# Write a program to swap values of two numbers entered by the user.

a = int(input("enter 1st value: "))
b = int(input("enter 2nd value: "))

#swaping 
temp = a
a = b
b = temp

print(f"Value of a : {a} \nvalue of b : {b}")   