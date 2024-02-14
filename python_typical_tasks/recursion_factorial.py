# Определение n-ного значения факториала
# Решение через рекурсию

def factorial(n: int) -> str | int:
    if n < 0:
        return "Введённое число должно быть нулём, либо быть положительным!"
    elif n < 2:
        return 1
    else:
        return n * factorial(n - 1)


def main():
    number = int(input("Введите исходное число: "))
    print(f'Факториал от {number} равен: ', factorial(number))


if __name__ == '__main__':
    main()
