from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print(f"{self.name} barks")

class Cat(Animal):
    def make_sound(self):
        print(f"{self.name} meows")

def animal_sounds(animal):
    animal.make_sound()

dog = Dog("Buddy")
cat = Cat("Whiskers")

animal_sounds(dog)  # Output: "Buddy barks"
animal_sounds(cat)  # Output: "Whiskers meows"
