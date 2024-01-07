import math


def main():
    x = math.pi / 3
    y = 4.021
    z = -5.72

    first_exp = math.cos(math.log10(math.fabs(math.sin((x * y * z) ** 5)))) ** 5
    second_exp = (first_exp ** (1 / 5)) - (10 ** (3 * z))
    third_exp = first_exp * (10 ** (-3 * z))
    a = second_exp / third_exp
    print(math.ceil(a))


if __name__ == '__main__':
    main()
