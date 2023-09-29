# ЗАМЕТКИ:
# Метод __init__ не конструктор, т.к. работает на уже созданном объекте;
# Если __repr__ и __str__ не реализованы по умолчанию возращается адрес памяти при выводе объекта;
# Метод __eq__ по умолчанию сравнивает адрес в памяти, в реализации лучше сразу проверить тип;
# Если методы сравнения не реализованы, падает ошибка;
# Метод __contains__ служит для реализации проверки in;
# Метод bool для самописных объектов по умолчанию всегда вернёт True;
# Метод len для самописных объектов не работает, падает ошибка;
# Метод __call__ позволяет сделать объект исполняемым(), без реализации падает ошибка;
# Метод __iter__ реализует тот, кто Iterable;
# Метод __next__ реализует тот, кто Iterator;
# Итератор лучше реализовывать отдельным классом, чтобы не держать всё в куче;
# Метод __getitem__ позволяет реализовать обращение по индексу/ключу для объекта. Если не реализован, падает ошибка;
# Метод __setitem__ позволяет присваивать значение по индексу/ключу для объекта. Если не реализован, падает ошибка;
# Метод __getitem__ также позволяет заменить работу Итератора для цикла for, если тот не реализован;


class Banknote:
    def __init__(self, value: int):  # инициализатор атрибутов класса
        self.value = value

    def __repr__(self):  # вывод объекта, как есть в коде, для программиста
        return f'Banknote({self.value})'

    def __str__(self):  # вывод объекта для пользователя в красивом виде
        return f'Банкнота номиналом в {self.value} рублей'

    def __eq__(self, other):
        if other is None or not isinstance(other, Banknote):
            return False
        return self.value == other.value

    # Реализация сравнений объектов
    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value

    def __le__(self, other):
        return self.value <= other.value

    def __ge__(self, other):
        return self.value >= other.value


class Wallet:
    def __init__(self, *banknotes: Banknote):
        self.container = []
        self.container.extend(banknotes)
        self.index = 0

    def __repr__(self):
        return f'Wallet({self.container})'

    def __contains__(self, item):  # проверка вхождения
        return item in self.container

    def __bool__(self):  # возвращает bool от объекта
        return len(self.container) > 0  # либо: return bool(self.container)

    def __len__(self):  # возвращает длину объекта
        return len(self.container)

    def __call__(self):  # позволяет вызывать объекты нашего класса через wallet()
        return f'В кошельке {sum(e.value for e in self.container)} рублей'

    def __iter__(self):  # возвращает объект итератора
        return Iterator(self.container)  # каждый раз будет возвращаться новый объект

    # def __next__(self):  # возвращает следующий элемент у объекта итератора
    #     if 0 <= self.index < len(self.container):
    #         value = self.container[self.index]
    #         self.index += 1
    #         return value
    #     raise StopIteration

    def __getitem__(self, item: int):  # возвращает элемент по индексу/ключу
        if item < 0 or item >= len(self.container):
            raise IndexError
        return self.container[item]

    def __setitem__(self, key: int, value: Banknote):  # позволяет устанавливать (присваивать) значения по индексу/ключу
        if key < 0 or key > len(self.container):
            raise IndexError
        self.container[key] = value


class Iterator:
    def __init__(self, container):
        self.container = container
        self.index = 0

    def __next__(self):  # возвращает следующий элемент у объекта итератора
        if 0 <= self.index < len(self.container):
            value = self.container[self.index]
            self.index += 1
            return value
        raise StopIteration


if __name__ == '__main__':
    banknote = Banknote(100)
    print(eval(repr(banknote)))  # вызовет str; eval использовать очень аккуратно!!!
    print(repr(banknote))

    fifty = Banknote(50)
    hundred = Banknote(100)
    print(fifty == hundred)
    print(banknote == hundred)
    print(fifty > banknote)
    print(fifty < banknote)
    print(banknote >= fifty)
    print(banknote <= hundred)

    wallet = Wallet(fifty, hundred, hundred)
    print(wallet)
    print(fifty in wallet)
    print(Banknote(1000) in wallet)
    print(bool(wallet))
    print(len(wallet))
    print(wallet())

    for money in wallet:
        print(money)

    print()

    print(wallet[0])
    # print(wallet[-1])  # упадёт ошибка, работа с отрицательными индексами была не реализована!
    wallet[0] = Banknote(500)
    print(wallet[0])