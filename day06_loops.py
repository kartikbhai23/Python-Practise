# Day 6: Loops
# practicing for and while loops today

# print 0 to 4 using range()
print("For loop:")
for i in range(5):
    print(i, end=" ")
print()

# countdown with while loop
print("While loop:")
count = 5
while count > 0:
    print(count, end=" ")
    count -= 1
print()

# testing break and continue
print("Break/Continue test:")
for number in range(1, 10):
    if number == 5:
        continue  # skip 5
    if number == 8:
        break  # exit loop
    print(number, end=" ")
print()

# exercise 1: sum from 1 to 50
total_sum = 0
for n in range(1, 51):
    total_sum += n
print("Sum is:", total_sum)

# exercise 2: multiplication table of 7
print("Table of 7:")
for multiplier in range(1, 11):
    print(f"7 x {multiplier} = {7 * multiplier}")

# challenge: find prime numbers up to 30
print("Primes up to 30:")
for num in range(2, 31):
    is_prime = True
    for divisor in range(2, int(num ** 0.5) + 1):
        if num % divisor == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
print()

# prime checker works for limit of 30
