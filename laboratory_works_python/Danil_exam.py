# Дана строка символов, признак конца строки –
# точка. Сформировать множество гласных букв, входящих в каждое слово строки более
# двух раз. Результаты сохранить в текстовый файл. (Не использовать структуру список)

def get_vows(string):
    vows = set()
    words = string.split()

    for word in words:
        counts = {}

        for letter in word:
            if letter.lower() in 'aeiouаеёиоуыэюя':
                counts[letter.lower()] = counts.get(letter.lower(), 0) + 1

        for letter, count in counts.items():
            if count > 2:
                vows.add(letter)

    return vows


def main():
    string = input("Введите исходную строку символов: ")
    vowels = get_vows(string)

    with open('result.txt', 'w') as file:
        file.write(''.join(vowels))


if __name__ == '__main__':
    main()
