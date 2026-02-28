# Day 18: Inheritance and polymorphism
# parent and child classes, overriding parent methods

# parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Generic sound"

# child inheriting parent
class Cat(Animal):
    def speak(self):
        return "Meow!"

class Cow(Animal):
    def speak(self):
        return "Moo!"

# poly test
animals = [Cat("Kitty"), Cow("Bessie"), Animal("Generic")]
for animal in animals:
    print(f"{animal.name}: {animal.speak()}")

# using super() in child class
class WildCat(Cat):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    def details(self):
        return f"Wild cat {self.name} ({self.size})"

tiger = WildCat("Sheru", "Large")
print(tiger.details())
print(tiger.speak())

# exercise 1: isinstance checks
print("Is tiger WildCat?", isinstance(tiger, WildCat))
print("Is tiger Cat?", isinstance(tiger, Cat))
print("Is tiger Animal?", isinstance(tiger, Animal))

# challenge: Employee and Manager classes
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        return f"Employee: {self.name}, Salary: ${self.salary}"

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Dept: {self.department}"

mgr = Manager("Alice", 95000, "Engineering")
print(mgr.display_info())

# checked employee inheritance hierarchy
