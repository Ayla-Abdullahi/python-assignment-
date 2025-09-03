# Base Class
class Smartphone:
    def __init__(self, brand, model, storage, battery):
        self.brand = brand
        self.model = model
        self.__storage = storage     # encapsulated (private) attribute
        self.battery = battery

    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number} ")

    def charge(self, amount):
        self.battery += amount
        print(f"{self.brand} {self.model} charged. Battery: {self.battery}%")

    def get_storage(self):
        return self.__storage  # getter for encapsulated attribute

# Subclass (Inheritance)
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, storage, battery, gpu):
        super().__init__(brand, model, storage, battery)
        self.gpu = gpu

    def play_game(self, game):
        if self.battery > 10:
            print(f"Playing {game} on {self.brand} {self.model} with {self.gpu} GPU 🎮")
            self.battery -= 10
        else:
            print("Battery too low to play games ")

# Demonstration of the classes above

phone1 = Smartphone("Samsung", "Galaxy S23", "256GB", 80)
phone1.call("123-456-789")
phone1.charge(10)
print("Storage:", phone1.get_storage())

gaming_phone = GamingSmartphone("Asus", "ROG Phone 7", "512GB", 50, "Adreno 740")
gaming_phone.play_game("Genshin Impact")
gaming_phone.charge(20)

# Activity 2 on polymorphism
# Base class
class Animal:
    def move(self):
        pass  # abstract action

class Dog(Animal):
    def move(self):
        print("Dog is running 🐕")

class Fish(Animal):
    def move(self):
        print("Fish is swimming 🐟")

class Bird(Animal):
    def move(self):
        print("Bird is flying 🐦")

# Polymorphism demo
animal = input("Enter the animal you want it to move (Dog, Fish, Bird): ")
if animal == "Dog":
    Dog().move()
elif animal == "Fish":
    Fish().move()
elif animal == "Bird":
    Bird().move()
else:
    print("Unknown animal.")
