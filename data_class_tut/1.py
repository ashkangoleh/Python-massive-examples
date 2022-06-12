from dataclasses import dataclass, field
import gc


@dataclass
class Person:
    name: str
    height_in_meters: float


# princess = Person("Diana Spencer", 1.8)
# john = Person("John Lockwood", 1.85)
# george = Person("George Washington", 1.88)
# rock = Person("Duane Johnson", 1.88)
#
# people = [princess, george, john, "Cheese Sandwich", rock]
#
# for person in people:
#     match person:
#         case Person("John Lockwood", 1.85) as me:
#             print(f"Found {me} by exact match.")
#         case Person(name, 1.88) as person:
#             print(f"Found by height: {name}.")
#         case Person(_, _):
#             print("Found Lady Di!")
#####################
# Here is the dataclass decorator’s signature, showing what arguments are available and their defaults:#
# def dataclass(*, init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False)
#####################
@dataclass(init=False)  # while init is False does not need pass object into class
class MyClass:
    my_field: int


my_var = MyClass()
my_var.my_field = 42
print(my_var.my_field)


@dataclass(frozen=True)  # while frozen is True , object cannot get attr or change
class MyClass2:
    my_field: int


my_var = MyClass2(42)
# my_var.my_field = 43 # Error
print(my_var.my_field)


# do not repr specific field
@dataclass()
class User:
    email: str
    password: str = field(repr=False)


player_one = User("ready_player_one@example.com", "secret123")
print(player_one)


@dataclass
class Rectangle:
    length: float
    width: float
    area: float = field(init=False, repr=False)

    def __post_init__(self):
        self.area = self.length * self.width

    @property
    def multiple(self):
        return self.area ** 2


couch = Rectangle(length=6.0, width=3.0)
print(couch.multiple)
print(f"A {couch} has area {couch.area.__hash__()}.")  # result = A Rectangle(length=6.0, width=3.0) has area 18.
print(f"A {couch} has area {couch.area}.")  # result = A Rectangle(length=6.0, width=3.0) has area 18.0.


# compare
@dataclass(order=True, init=True)
class PersonByHeight:
    name: str = field(compare=False)
    height_in_meters: float


abe = PersonByHeight("abe", 1.93)
john = PersonByHeight("john", 1.85)

print(f"abe > john: {abe > john}")

print(gc.collect())
