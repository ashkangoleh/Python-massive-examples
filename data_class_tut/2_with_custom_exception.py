from dataclasses import dataclass


@dataclass
class VacationDaysShortageError(Exception):
    requested_days: int
    remaining_days: int

    def __str__(self):
        return f"\nrequested days: {self.requested_days}\nremaining days: {self.remaining_days}"


@dataclass
class Employee:
    name: str
    vacation_days: int = 25

    def take_holiday(self, days: int = 1) -> None:
        if self.vacation_days < days:
            raise VacationDaysShortageError(
                requested_days=days, remaining_days=self.vacation_days
            )
        self.vacation_days -= days
        print("have fun on your holiday")


def main() -> None:
    ashkan = Employee(name="ashkan")
    ashkan.take_holiday(25)


if __name__ == "__main__":
    main()
