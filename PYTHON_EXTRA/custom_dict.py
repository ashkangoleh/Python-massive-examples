from collections import UserDict


class UpperCaseKey(UserDict):
    def __setitem__(self, key, value) -> None:
        key = key.upper()
        super().__setitem__(key, value)

_dict = {
    "name": "x", "age": 2,
}
numbers = UpperCaseKey(_dict)


numbers["three"] = 3
numbers.update({"four": 4})
numbers.setdefault("five", 5)

print(numbers)

