# Вам дано число N. Напишите скрипт, который считал бы сумму всех четных чисел в промежутке от 1 до N, включая N.
# К примеру, если N равняется 6, то вывод должен быть равен 2+4+6, то есть 12.

def summ_numbers(n: int) -> int:
    if n < 0:
        raise 'Введённое число должно быть положительным!'
    else:
        i = 2
        summ = 0
        while i <= n:
            summ += i
            i += 2

        return summ


def main():
    number = int(input("Введите число N: "))
    print("Сумма всех чисел от 1 до N равна: ", summ_numbers(number))


if __name__ == '__main__':
    main()
