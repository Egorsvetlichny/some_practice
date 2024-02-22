# У вас есть строка STR, в которой есть слова с пробелами.
# Вам нужно заменить пробелы между словами на “@40”.

def space_replace(string: str) -> str:
    if ' ' not in string:
        return 'Исходная строка не содержит пробелов!'

    return string.replace(' ', '@40')


def main():
    string1 = (input("Введите исходную строку: "))
    print(space_replace(string1))


if __name__ == '__main__':
    main()
