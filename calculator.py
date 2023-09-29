# Функция-калькулятор для двух целых чисел

def calculator(expression: str):
    alowed = '+-*/'
    if not any(symbol in alowed for symbol in expression):
        raise ValueError(f'Выражение должно содержать хотя бы один знак ({alowed})')
    for symbol in alowed:
        if symbol in expression:
            try:
                left, right = expression.split(symbol)
                left, right = int(left), int(right)
                return {
                    '+': lambda a, b: a + b,
                    '-': lambda a, b: a - b,
                    '*': lambda a, b: a * b,
                    '/': lambda a, b: a / b
                }[symbol](left, right)

                # if symbol == '+':
                #     return left + right
                # elif symbol == '*':
                #     return left * right
                # elif symbol == '-':
                #     return left - right
                # elif symbol == '/':
                #     return left / right

            except (ValueError, TypeError):
                raise ValueError('Выражение должно содержать 2 целых числа и 1 знак')


if __name__ == '__main__':
    print(calculator('10 * 20'))

    assert calculator('10 * 20') == 200
    assert calculator('100-5') == 95
    assert calculator('5 + 6') == 11
    assert calculator('10 / 2') == 5
