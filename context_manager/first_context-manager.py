# Реализация контекст-менеджера для следующей задачи:
# Если размер вектора v1 равен размеру вектора v2, тогда добавить к вектору v1 вектор v2,
# иначе оставить вектор v1 без изменений.

class DefendedVector:
    def __init__(self, v):
        self.__v = v

    def __enter__(self):
        self.temp = self.__v[:]
        return self.temp

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.__v[:] = self.temp

        return False  # если True - исключения будут обрабатываться внутри контекст-менеджера


if __name__ == '__main__':
    v1 = [1, 4, 2]
    v2 = [2, 5, '6']

    try:
        with DefendedVector(v1) as dv:
            if len(dv) == len(v2):
                for i, el in enumerate(dv):
                    dv[i] += v2[i]
            else:
                raise IndexError
    except IndexError:
        print("Размер вектора v1 не равен размеру вектора v2")
    except Exception:
        print("Ошибка при сложении векторов!")

    print(f'v1 = {v1}', f'v2 = {v2}', sep='\n')
