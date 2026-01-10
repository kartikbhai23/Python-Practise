class Laptop:
      count = 0

      def __init__(self, brand, Price, ram, storage):
                self.brand = brand
                self.Price = Price
                self.ram = ram
                self.storage = storage
                Laptop.count += 1

l1 = Laptop("Dell", 800, "16GB", "512GB")
l2 = Laptop("HP", 750, "8GB", "256GB")
print("Total number of Laptop instances created:", Laptop.count) 