class Singleton_Genius(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not Singleton_Genius.__instance:
            Singleton_Genius.__instance = object.__new__(cls)
        return Singleton_Genius.__instance

    def __init__(self, name, lastname) -> None:
        self.name = name
        self.lastname = lastname


s1 = Singleton_Genius("ashkan", "goleh")
s2 = Singleton_Genius("ashkan", "goleh pour")
s3 = Singleton_Genius("ashkan", "unreboot")
print(s3 == s2)


print("==>> s1: ", s1)
print("==>> s2: ", s2)
print("==>> s3: ", s3)

print("==>> s1.lastname: ", s1.lastname)
print("==>> s2.lastname: ", s2.lastname)
print("==>> s3.lastname: ", s3.lastname)
