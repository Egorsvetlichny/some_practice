class ReadToInt:  # class non-data-discriptor
    def __set_name__(self, owner, name):
        self.name = '_x'

    def __get__(self, instance, owner):
        return getattr(instance, self.name)


class Integer:  # class data-discriptor
    @classmethod
    def verify_cord(cls, cord):
        if type(cord) != int:
            raise TypeError('координата должна быть целым числом!')

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.verify_cord(value)
        setattr(instance, self.name, value)


class Point3D:
    x = Integer()
    y = Integer()
    z = Integer()
    xr = ReadToInt()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f'x = {self.x}, y = {self.y}, z = {self.z}'


if __name__ == '__main__':
    pt = Point3D(1, 2, 3)
    print(pt)
    print(pt.xr)
    print(pt.__dict__)
