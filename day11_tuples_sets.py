# Day 11: Tuples and Sets
# tuples are read-only lists (immutable). sets only store unique items.

# tuple creation
my_tuple = ("python", "java", "c++")
print("Tuple items:", my_tuple)

# set creation
my_set = {"apple", "banana", "cherry", "apple"}
print("Set (removed duplicates):", my_set)

# set operations like math union/intersection
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print("Union:", set_a.union(set_b))
print("Intersection:", set_a.intersection(set_b))
print("Difference (A - B):", set_a.difference(set_b))

# exercise 1: tuple unpacking
coordinates = (10, 20, 30)
x, y, z = coordinates
print(f"Unpacked values: X={x}, Y={y}, Z={z}")

# challenge: clean duplicates from list and sort it
def get_sorted_unique(items):
    unique_set = set(items)
    unique_list = list(unique_set)
    unique_list.sort()
    return unique_list

raw_data = [5, 2, 9, 2, 5, 8, 1, 9]
print("Raw data list:", raw_data)
print("Sorted unique list:", get_sorted_unique(raw_data))
