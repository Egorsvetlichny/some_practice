def divide(a: int, b: int) -> int:
    """
    Делит первое число на второе и возвращает результат
    :param a: целое число (делимое)
    :param b: целое число (делитель)
    :return: результат деления (частное)
    :raises ValueError: если делитель равен нулю

    >>> divide(10, 5)
    2
    >>> divide(100, 2)
    50

    """
    if b == 0:
        raise ValueError('делить на 0 нельзя')
    return a // b