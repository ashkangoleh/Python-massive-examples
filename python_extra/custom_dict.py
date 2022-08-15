from collections import UserDict


class UpperCaseDict(UserDict):
    def __setitem__(self, key, value) -> None:
        key = key.upper()
        # value = value ** 2
        super().__setitem__(key, value)


numbers = UpperCaseDict({
    "one": 1, "two": 2,
})


numbers["three"] = 3
numbers.update({"four": 4})
numbers.setdefault("five", 5)

print(numbers)

