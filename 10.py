""""
Take a decimal number as input (like ) and output its: 
45.78 
• integer part - 45 
• fractional part - .78 
"""
a = float(input("enter the decimal num: "))

b = int(a)

c = float(a - b)

print(f"Integer part : {b} \nFractional part : {c}")