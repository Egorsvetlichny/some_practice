# Определить значение n-ного элемента в последовательности Фибоначи

def fibonacci_numbers(n: int):
    if n < 1:
        return "Неправильно введён номер числа в последовательности. Минимальный номер числа 1"
    elif n <= 2:
        return 1
    else:
        number1 = 1
        number2 = 1
        i = 2
        while i != n:
            if i % 2 != 0:
                number1 += number2
            else:
                number2 += number1

            i += 1

        return max(number1, number2)


def main():
    number = int(input('Введите номер числа в последовательности Фибоначи: '))
    print(f"Число в последовательности Фибоначи под номером {number} равно: ", fibonacci_numbers(number))


if __name__ == '__main__':
    main()
