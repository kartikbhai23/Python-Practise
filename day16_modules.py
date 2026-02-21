# Day 16: Modules
# importing math, random, and datetime libraries

import math
import random
from datetime import datetime

# math helpers
print("Sqrt of 64:", math.sqrt(64))
print("Pi:", math.pi)
print("Ceil of 4.2:", math.ceil(4.2))

# random generation
random.seed(42)
print("Random float:", random.random())
print("Random int [1, 100]:", random.randint(1, 100))
options = ["Red", "Green", "Blue"]
print("Random choice:", random.choice(options))

# current dates
now = datetime.now()
print("Now date:", now)
print("Formatted date:", now.strftime("%d-%m-%Y %H:%M:%S"))

# exercise 1: circle area using math.pi
radius = 7
area = math.pi * (radius ** 2)
print(f"Circle Area: {area:.3f}")

# challenge: custom password generator
def generate_password(length=8):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01233456789!@#$"
    password = "".join(random.choice(chars) for _ in range(length))
    return password

print("Password generator output:", generate_password(12))
