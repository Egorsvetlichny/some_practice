import copy


class Adress:
    def __init__(self, street_adress, city, country):
        self.street_adress = street_adress
        self.city = city
        self.country = country

    def __str__(self):
        return f'{self.street_adress}, {self.city}, {self.country}'


class Person:
    def __init__(self, name, adress):
        self.name = name
        self.adress = adress

    def __str__(self):
        return f'{self.name} lives at {self.adress}'


if __name__ == '__main__':
    john = Person('John', Adress('123 London Road', 'London', 'UK'))
    print(john)
    print()

    # jane = john
    # jane.name = 'Jane'
    # print(jane)
    # print(john)

    jane = copy.deepcopy(john)  # используем deepcopy для полного копирования объекта со всеми внутренними ссылками
    jane.name = 'Jane'
    jane.adress.city = 'Brooklin'
    print(jane)
    print(john)
