"""
Q8. Let's create a Simple Calculator that performs arithmetic operations. Create 
a function calculator(a, b, operation) that performs addition, subtraction, 
multiplication, or division based on the operation parameter. 

[operation parameter can have values "add", "subtract", "multiply", or "divide".  ]
"""

def calculator(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operation"

a = int(input('enter the 1st number: '))
b = int(input('enter the 2nd number: '))
c = input("Enter the operation (add, subtract, multiply, divide): ")

calculator(a, b, c)