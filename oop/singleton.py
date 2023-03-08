class SingletonGenius(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not SingletonGenius.__instance:
            SingletonGenius.__instance = object.__new__(cls)
        return SingletonGenius.__instance

    def __init__(self, name, lastname) -> None:
        self.name = name
        self.lastname = lastname
        
    def __repr__(self) -> str:
        return f"{self.name!r} {self.lastname!r}"
class Singleton:
    instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

s1 = Singleton()
s2 = Singleton()

print(s1 is s2) # prints True
print(s1 == s2)

s1 = SingletonGenius("ashkan", "goleh")
s2 = SingletonGenius("ashkan", "goleh pour")
s3 = SingletonGenius("ashkan", "unreboot")
print(s1)
print(s3)
print(s3 == s2)


# print("==>> s1: ", s1)
# print("==>> s2: ", s2)
# print("==>> s3: ", s3)

# print("==>> s1.lastname: ", s1.lastname)
# print("==>> s2.lastname: ", s2.lastname)
# print("==>> s3.lastname: ", s3.lastname)


# class test:

#     __state = {}

#     def __init__(self):
#         self.__dict__ = self.__state
#         if not hasattr(self, 'ashkan'):
#             self.ashkan = "ashkan11"


# class Person:
#     name = "John"
#     age = 36
#     country = "Norway"


# x = hasattr(Person, 'age')
# print("==>> x: ", x)

# c = test()

# print(c.ashkan)
