#Ask the user to enter two integers and one float. Convert them all to floats  and print their average. 

a = int(input("enter the 1st num :"))
b = int(input("enter the 2nd num :"))
c = float(input("enter the 3rd num :"))

avg = float((a*b*c)/2)

print(f"Average of {a} , {b} & {c} = {avg}")