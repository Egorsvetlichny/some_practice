def main():
    counter = 0
    previous_symbol = None

    while True:
        symbol = input("Введите символ: ")

        if symbol == '0':
            break
        else:
            symbol_number = ord(symbol)

            if previous_symbol is None:
                previous_symbol = symbol_number
                continue
            elif symbol_number == previous_symbol + 1:
                counter += 1

            previous_symbol = symbol_number

    print("Количество пар следующих друг за другом символов:", counter)


if __name__ == '__main__':
    main()
