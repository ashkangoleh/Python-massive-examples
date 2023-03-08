class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = age

person = Person("John", 30)

print(person.get_name())  # Output: "John"
person.set_name("Jane")
print(person.get_name())  # Output: "Jane"

print(person.get_age())  # Output: 30
person.set_age(35)
print(person.get_age())  # Output: 35
