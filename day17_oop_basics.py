# Day 17: Class basics
# learning OOP concepts: classes, instances, constructors

class Dog:
    species = "Canine"

    # setting up name and breed instance fields
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    # instance methods
    def bark(self):
        return f"{self.name} says Woof!"

    def get_details(self):
        return f"Name: {self.name}, Breed: {self.breed}, Species: {self.species}"

# testing instance creation
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Rocky", "German Shepherd")

print(dog1.bark())
print(dog2.get_details())

# changing properties directly
dog1.name = "Max"
print("Updated name:", dog1.name)

# exercise 1: updating breed attribute
dog1.breed = "Labrador"
print("Updated dog1 breed info:", dog1.get_details())

# challenge: Car odometer class tracking
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def description(self):
        return f"{self.year} {self.make} {self.model}"

    def drive(self, distance):
        if distance > 0:
            self.odometer += distance
        return self.odometer

my_car = Car("Toyota", "Corolla", 2020)
print("Car info:", my_car.description())
my_car.drive(150)
my_car.drive(75)
print("Car odometer reading:", my_car.odometer)
