# Определить значение n-ного элемента в последовательности Фибоначи.
# Решение через рекурсию.

def fibonacci_numbers(n: int):
    if n < 1:
        return "Неправильно введён номер числа в последовательности. Минимальный номер числа 1"
    elif n <= 2:
        return 1
    else:
        return fibonacci_numbers(n - 1) + fibonacci_numbers(n - 2)


def main():
    number = int(input('Введите номер числа в последовательности Фибоначи: '))
    print(f"Число в последовательности Фибоначи под номером {number} равно: ", fibonacci_numbers(number))


if __name__ == '__main__':
    main()
