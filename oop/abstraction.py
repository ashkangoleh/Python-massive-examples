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


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass
    
# if i remove perimeter from Rectangle i'll raise TypeError like 'TypeError: Can't instantiate abstract class Rectangle with abstract method perimeter'
# because its inheritance of Shape ABC class

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

# Usage
r = Rectangle(5, 10)
print("Rectangle Area:", r.area())
print("Rectangle Perimeter:", r.perimeter())
print(r.test())
c = Circle(7)
print("Circle Area:", c.area())
print("Circle Circumference:", c.perimeter())