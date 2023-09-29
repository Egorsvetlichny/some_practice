# Реализация для замера скорости работы произвольной функции
import time


def test_time_decorator(func):
    def wrapper(*args, **kwargs):
        st = time.time()
        res = func(*args, **kwargs)
        et = time.time()
        dt = et - st
        print(f'Время работы функции равно {dt} секунд')
        return res

    return wrapper


# Медленный алгоритм Евклида (находит НОД двух чисел)
@test_time_decorator
def get_nod(number1, number2):
    while number1 != number2:
        if number1 > number2:
            number1 -= number2
        else:
            number2 -= number1
    return number1


# Быстрый алгоритм Евклида
@test_time_decorator
def get_fast_nod(number1, number2):
    if number1 < number2:
        number1, number2 = number2, number1
    while number2:
        number1, number2 = number2, number1 % number2
    return number1


if __name__ == '__main__':
    a, b = 2, 10000000
    print('НОД чисел a и b равен', get_nod(a, b))
    print('НОД чисел a и b равен', get_fast_nod(a, b))
