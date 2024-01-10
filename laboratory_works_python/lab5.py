def main():
    n = int(input("Введите количество столбцов матрицы A: "))
    m = int(input("Введите количество строк матрицы A: "))
    h = int(input("Введите целое число H: "))
    a = []

    for i in range(m):
        row = []
        for j in range(n):
            num = int(input(f"Введите элемент матрицы [{i}][{j}]: "))
            row.append(num)
        a.append(row)

    num_columns = len(a[0])
    columns_with_num = []
    columns_without_num = []

    for j in range(num_columns):
        has_num = False
        for i in range(len(a)):
            if a[i][j] == h:
                has_num = True
                break

        columns_with_num.append(j) if has_num else columns_without_num.append(j)

    print(f"Номера столбцов, содержащие число {h}: {columns_with_num}")
    print(f"Номера столбцов, не содержащие число {h}: {columns_without_num}")


if __name__ == '__main__':
    main()
