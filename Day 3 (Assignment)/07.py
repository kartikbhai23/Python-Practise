# Q7. Design a program to continuously input a number from user & print if it is  positive or negative until the user enters “Quit”. 

while True:
    user_input = input("Enter a number or type 'Quit' to stop: ")

    if user_input == "Quit":
        print("Program stopped.")
        break

    number = int(user_input)

    if number > 0:
        print("Positive number")
    elif number < 0:
        print("Negative number")
    else:
        print("Zero")
