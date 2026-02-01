# Day 10: Lists and comprehensions
# storing lists of items and doing operations on them

fruits = ["apple", "banana", "cherry"]
print("Initial list:", fruits)

# change banana to blueberry
fruits[1] = "blueberry"
print("Changed list:", fruits)

# adding elements
fruits.append("orange")
fruits.insert(1, "grapes")
print("After methods:", fruits)

# pop last item
removed = fruits.pop()
print(f"Removed '{removed}'. List: {fruits}")

# slicing lists
numbers = [10, 20, 30, 40, 50, 60]
print("Slice [1:4]:", numbers[1:4])
print("Reverse list using slicing:", numbers[::-1])

# list comprehension to calculate squares
squares = [x**2 for x in range(1, 6)]
print("Squares:", squares)

# exercise 1: filter out odd numbers
nums = [12, 15, 22, 9, 30, 45]
evens = [n for n in nums if n % 2 == 0]
print("Evens list:", evens)

# challenge: second largest element without sorting
def find_second_largest(numbers_list):
    if len(numbers_list) < 2:
        return None
    largest = second = float('-inf')
    for num in numbers_list:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num
    return second

test_list = [20, 45, 10, 45, 33, 8]
print(f"Second largest: {find_second_largest(test_list)}")
