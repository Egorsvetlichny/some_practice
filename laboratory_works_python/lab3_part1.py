def main():
    string = input("Введите исходную строку: ")
    words_arr = string.split()
    reverse_words_arr = []

    for item in words_arr:
        reverse_words_arr.append(item[::-1])

    string = ' '.join(reverse_words_arr)
    print(string)


if __name__ == '__main__':
    main()
