class Meta(type):
    def create_local_attrs(self, *args, **kwargs):
        for key, value in self.class_attrs.items():
            self.__dict__[key] = value

    def __init__(cls, name, base, attrs):
        cls.class_attrs = attrs
        cls.__init__ = Meta.create_local_attrs


class Women(metaclass=Meta):
    titele = 'Заголовок'
    content = 'Контент'
    photo = 'Путь к фото'


if __name__ == '__main__':
    w1 = Women()
    print(w1.__dict__)