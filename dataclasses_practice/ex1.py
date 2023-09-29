from pprint import pprint
from dataclasses import dataclass, field

class Thing:
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    def __repr__(self):
        return f'Thing: {self.__dict__}'


@dataclass
class ThingData:
    name: str
    weight: int
    price: float = 0
    dims: list = field(default_factory=list)


if __name__ == '__main__':
    td1 = ThingData('Учебник по Питону', 100, 1234.54)
    t = Thing('Учебник по Питону', 100, 1234.54)
    td1.dims.append(10)
    td2 = ThingData('Учебник по Питону', 100)
    print(td2.dims)