class Monostate:  # many objects, but one state
    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state
        if not self._shared_state:
            print('do some hard work')
            # parse, db, work with data/resourses etc...
            self.data = 100


if __name__ == '__main__':
    first = Monostate()
    print(first)
    second = Monostate()
    print(second)

    print(first is second)

    print(first.data)
    first.data = 'some text'
    print(second.data)

    print(Monostate())

    print(first.data == second.data)