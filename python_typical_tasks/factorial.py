# Определение n-ного значения факториала

def factorial(n: int) -> str | int:
    if n < 0:
        return "Введённое число должно быть нулём, либо быть положительным!"
    else:
        res = 1
        for i in range(1, n + 1):
            res *= i

        return res


def main():
    number = int(input("Введите исходное число: "))
    print(f'Факториал от {number} равен: ', factorial(number))


if __name__ == '__main__':
    main()
