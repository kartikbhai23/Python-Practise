# Day 20: Generators
# creating iterators easily using 'yield' inside functions

# simple generator
def simple_generator():
    yield "First"
    yield "Second"
    yield "Third"

gen = simple_generator()
print("Yields:")
print(next(gen))
print(next(gen))
print(next(gen))

# squares generator
def square_generator(limit):
    n = 1
    while n <= limit:
        yield n ** 2
        n += 1

print("Squares:")
for sq in square_generator(5):
    print(sq, end=" ")
print()

# exercise 1: generator expressions
cubes_gen = (x**3 for x in range(1, 6))
print("Cubes list:", list(cubes_gen))

# challenge: Fibonacci generator
def fibonacci_gen(limit):
    a, b = 0, 1
    count = 0
    while count < limit:
        yield a
        a, b = b, a + b
        count += 1

print("Fibonacci sequence generator:")
for f in fibonacci_gen(10):
    print(f, end=" ")
print()
