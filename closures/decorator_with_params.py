# Реализация декоратора с параметрами

from functools import wraps
import math


# декоратор для нахождения производной произвольной функции
def df_decorator(dx=0.01):
    def func_decorator(func):
        @wraps(func)  # позволяет сохранять имя функциии и её документацию после декорирования
        def wrapper(x, *args, **kwargs):
            res = (func(x + dx, *args, **kwargs) - func(x, *args, **kwargs)) / dx
            return res

        # wrapper.__name__ = func.__name__
        # wrapper.__doc__ = func.__doc__

        return wrapper

    return func_decorator


@df_decorator(dx=0.0001)
def sin_df(x):
    '''Функция для вычисления производной синуса'''
    return math.sin(x)


if __name__ == '__main__':
    print(sin_df(math.pi / 3))
    print(sin_df.__name__)
    print(sin_df.__doc__)
