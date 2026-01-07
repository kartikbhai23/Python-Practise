"""
. The user enters a string containing a number (e.g. "45" ). Convert it to: 
- an integer
- a float
- a string again 
Print all three values with their types. 
"""

a = "45"
b = int(a)
c = float(b)
d = str(c)

print(type(b))
print(type(c))
print(type(d))