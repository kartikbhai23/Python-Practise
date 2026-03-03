# Day 19: Iterators
# learning iter() and next() protocols, implementing custom iterators

numbers = [1, 2, 3]
iterator = iter(numbers)
print("Iterator type:", type(iterator))

print(next(iterator))
print(next(iterator))
print(next(iterator))

# custom countdown iterator class
class CountDown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        val = self.current
        self.current -= 1
        return val

print("Custom count loop:")
counter = CountDown(3)
for num in counter:
    print(num)

# exercise 1: manual string iter
chars = "Hi"
char_iter = iter(chars)
print(next(char_iter))
print(next(char_iter))

# challenge: Custom even number iterator
class EvenNumbers:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.limit:
            raise StopIteration
        val = self.current
        self.current += 2
        return val

print("Evens up to 10:")
for num in EvenNumbers(10):
    print(num, end=" ")
print()
