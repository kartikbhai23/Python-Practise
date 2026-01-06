""""
Ask the user for a temperature in Celsius (string input). Convert it to , 
then calculate and print temperature in Fahrenheit. 
float 
Conversion formula: FahrenheitTemp = (CelsiusTemp ∗ (9/5)) + 
32
"""
a = input("enter the temperature (Celsius): ")
b= int(a)
form = (b*(9/5) + 32)

print(f"The Temperature is (Fahrenheit): {form}")