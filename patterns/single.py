class Singleton:  # one object
    instance = None

    def __new__(cls):
        if Singleton.instance is None:
            Singleton.instance = super().__new__(cls)
            Singleton._do_work(Singleton.instance)
        return Singleton.instance

    def _do_work(self):
        print('do some hard work')
        # parse, db, work with data/resourses etc...
        self.data = 100


if __name__ == '__main__':
    first = Singleton()
    print(first)
    second = Singleton()
    print(second)

    print(first is second)

    print(first.data)
    first.data = 'some text'
    print(second.data)

    print(Singleton())

    print(first.data == second.data)