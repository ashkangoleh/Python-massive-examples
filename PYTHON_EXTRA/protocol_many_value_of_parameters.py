from typing import Protocol, Callable
from dataclasses import dataclass


def somthing_test(number:int|None)->int| None:
    return number*12

SomthingTestFn = Callable[[int],None]


def main(*,sth:SomthingTestFn,number:int):
    statement = sth(number)
    return statement



print(main(sth=somthing_test,number=100))

@dataclass
class Customer:
    name: str
    phone: str
    number: str
    exp_month: int
    exp_year: int
    valid: bool = False

class CardId(Protocol):
    @property
    def number(self) -> str:
        ...

    @property
    def exp_month(self) -> int:
        ...

    @property
    def exp_year(self) -> int:
        ...


def validate_card_id(card: CardId):
    return {
        "number": card.number,
        "exp_month": card.exp_month,
        "exp_year": card.exp_year
    }

customer = Customer(
    "ashkan",
    "999",
    "123",
    1,2
)
print(validate_card_id(customer))
