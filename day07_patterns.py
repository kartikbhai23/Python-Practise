# Day 7: Pattern printing
# nested loops are tricky but trying to print stars/numbers

# pattern 1: right triangle
rows = 4
print("Triangle:")
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end="")
    print()

# pattern 2: number repeat pyramid
print("\nNumber pyramid:")
for i in range(1, 5):
    for j in range(i):
        print(i, end="")
    print()

# exercise 1: 5x5 hash grid
print("\nSquare of #:")
for i in range(5):
    for j in range(5):
        print("#", end=" ")
    print()

# challenge: inverted triangle
print("\nInverted triangle:")
n = 4
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end="")
    print()
