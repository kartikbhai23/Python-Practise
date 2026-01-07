""""
Q10. Let's create a “Number Guessing Game”. Given a secret number (already 
decided by you), write a program that asks the user to guess it and prints: 
"Too high" 
"Too low" 
if the guess is above the number 
if the guess is below 
• 
"Correct!" 
if the guess matches
"""

print("Number Guessing Game")
a = int(input("Enter the number: "))

a = 69

if  0 < a :
    print("Too low")

elif a < 100:
    print("Too high")

else :
    print("Correct!")