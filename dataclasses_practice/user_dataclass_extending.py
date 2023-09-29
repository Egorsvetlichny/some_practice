from dataclasses import dataclass, field
from typing import Any


class GoodsMethodFactory:
    @staticmethod
    def get_init_mesure():
        return [0, 0, 0]


@dataclass
class Goods:
    current_uid = 0

    uid: int = field(init=False)
    price: Any = None
    weight: Any = None

    def __post_init__(self):
        print('Goods: post_init')
        Goods.current_uid += 1
        self.uid = Goods.current_uid


@dataclass
class Book(Goods):
    title: str = ''
    author: str = ''
    price: float = 0
    weight: float = 0
    measure: list = field(default_factory=GoodsMethodFactory.get_init_mesure)

    def __post_init__(self):
        super().__post_init__()
        print('Book: post_init')


if __name__ == '__main__':
    book = Book(1000, 100.54, 'Python OOP', 'Svetlichnyy E.A.', [5, 45, 54.5])
    print(book)