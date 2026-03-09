# Day 21: Decorators
# modifying function behavior without rewriting function logic

# simple logger decorator
def my_decorator(func):
    def wrapper():
        print("[Log] pre-call wrapper trigger")
        func()
        print("[Log] post-call wrapper trigger")
    return wrapper

@my_decorator
def say_hello():
    print("  Hello, World!")

say_hello()

# decorator wrapping functions with args
def double_result(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return res * 2
    return wrapper

@double_result
def add(a, b):
    return a + b

print("add(5, 3) doubled:", add(5, 3))

# exercise 1: print function name on execution
def print_func_name(func):
    def wrapper(*args, **kwargs):
        print(f"Executing: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@print_func_name
def test_function():
    return "Done"

print(test_function())

# challenge: function execution timer decorator
import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Took {end - start:.6f} seconds to complete.")
        return result
    return wrapper

@timer_decorator
def heavy_calculation():
    total = 0
    for i in range(1000000):
        total += i
    return total

print("Result:", heavy_calculation())
