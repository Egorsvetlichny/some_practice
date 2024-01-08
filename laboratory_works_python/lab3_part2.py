def main():
    x = list(map(lambda x: int(x), input("Введите (через пробел) исходный массив: ").split()))
    y = []
    counter = 0

    for i in range(len(x) - 1):
        if x[i] == x[i + 1]:
            counter += 1
            y.append((x[i], x[i + 1]))

    # y = sorted(y, key=lambda item: item)
    y.sort()

    print(f"Количество пар соседних одинаковых элементов: {counter}")
    print(f"Массив y, содержащий пары: {y}")


if __name__ == '__main__':
    main()
