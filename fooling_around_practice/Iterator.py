class MyIterator:
    def __init__(self, start=0, stop=0, step=1):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        self.value = self.start - self.step
        return self

    def __next__(self):
        if self.value + self.step < self.stop:
            self.value += self.step
            return self.value
        else:
            raise StopIteration


class FRange2D:
    def __init__(self, start=0, stop=0, step=1, rows = 5):
        self.rows = rows
        self.fr = MyIterator(start, stop, step)

    def __iter__(self):
        self.value = 0
        return self

    def __next__(self):
        if self.value < self.rows:
            self.value += 1
            return iter(self.fr)
        else:
            raise StopIteration


if __name__ == '__main__':
    fr = FRange2D(0, 2.5, 0.5, 9)
    for x in fr:
        for i in x:
            print(i, end=' ')
        print()
