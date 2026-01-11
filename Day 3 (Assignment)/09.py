"""
Q9. Write a function  is_prime(n) that returns True if n is a prime number and 
False otherwise, using a loop.
[Hint -  
1. We only check prime for 2 or numbers greater than 2. is the smallest 
prime number. 
2. A non-Prime number, , will always get divided by atleast one number in 
range [2, n-1]. 
Eg - For number we'll check in range (2, 8) & it'll get divided by 3. So is 
non-prime & we'll return false for it. 
For number we'll check in range (2, 6) & it won't get divided by any. So 
is prime & we'll return true for it. ]
"""
input_number = int(input("Enter a number to check if it is prime: "))
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
result = is_prime(input_number)
if result:
    print(f"{input_number} is a prime number.")
else:
    print(f"{input_number} is not a prime number.")
