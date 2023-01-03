from typing import Self


class Fruit:
    def __init__(self, name: str):
        self.name = name

    @classmethod
    def from_string(cls, name: str, power: int) -> Self:
        power_fruit: str = f"{name}{'!'*power}"
        return cls(power_fruit)

    def __enter__(self) -> Self:
        return self

    def change_name(self, name: str) -> Self:
        self.name = name
        return self.name


if __name__ == "__main__":
    fruit: Fruit = Fruit.from_string("banana", 10)
    print(fruit.name)
