""""
Ask the user for: Principal (P), Rate (R), Time (T). Convert all to and 
compute simple interest: 
SI = (P * R * T )/100 
"""
p = int(input("enter the principal: "))
r = int(input("enter the rate: "))
t = int(input("enter the time: "))

si = (p*r*t)/100

print(f"the simple intrest is : {si}")