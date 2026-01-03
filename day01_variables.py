# Day 1: Variables and comments
# Starting my python journey today. Learning how to store variables.

# setting up some variables
x = 5
y = 10.5
name = "Kartik"
is_learning = True

print("My name is", name)
print("x is:", x)
print("y is:", y)
print("Am I learning?", is_learning)

# let's change x and see what happens
x = 100
print("Now x is changed to:", x)

# exercises from the lesson
# 1. create variable for age and print it
age = 20
print("My age is:", age)

# 2. swapping two numbers. used a temp variable for this
a = 1
b = 2
print("Before swap: a =", a, "b =", b)
temp = a
a = b
b = temp
print("After swap: a =", a, "b =", b)

# challenge: finding the area of a rectangle
length = 15
width = 8
area = length * width
print("Area of rectangle:", area)
