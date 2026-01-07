""""

Write a program that takes as input. Using conditional statements, 
calculate the final tax rate based on these rules: 
• If salary < 30,000 → 5% 
• If salary is 30,000–70,000 → 15% 
• If salary > 70,000 → 25%

"""
salary = float(input("Enter your salary: "))

if salary < 30000:
    tax = salary * 0.05
    tax_rate = 5

elif 30000 <= salary <= 70000:
    tax = salary * 0.15
    tax_rate = 15

else:
    tax = salary * 0.25
    tax_rate = 25

print("Tax Rate:", tax_rate, "%")
print("Tax Amount:", tax)