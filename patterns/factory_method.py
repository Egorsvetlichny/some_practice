# Фабричный метод - патерн проектирования, это любой метод создающий объект.
# Фабричный метод - альтернатива конструктору, имеющая множество преимуществ.
# Например - нэйминг (более удобное наименование аргументов).
# "Лучше использовать эти крошечные статические методы, которые могут инициализировать объект за вас"

from enum import Enum
from math import cos, sin


class CoordinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # def __init__(self, x, y, system = CoordinateSystem.CARTESIAN):
    #     if system == CoordinateSystem.CARTESIAN:
    #         self.x = x
    #         self.y = y
    #     elif system == CoordinateSystem.POLAR:
    #         self.x = x * cos(y)
    #         self.y = x * sin(y)

    def __str__(self):
        return f'x: {self.x}, y: {self.y}'

    @staticmethod
    def new_cartesian_point(x, y):
        return Point(x, y)

    @staticmethod
    def new_polar_point(rho, theta):
        return Point(rho * cos(theta), rho * sin(theta))


if __name__ == '__main__':
    p = Point(2, 3)
    print(p.__dict__)
    p1 = Point.new_cartesian_point(5, 10)
    p2 = Point.new_polar_point(5, 10)
    print(p1, p2, sep='\n')
