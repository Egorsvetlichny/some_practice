def define_new_array(arr1, arr2):
    res = []
    i = 0
    j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] > arr2[j]:
            res.append(arr1[i])
            i += 1
        elif arr1[i] < arr2[j]:
            j += 1
        else:
            i += 1
            j += 1

    while i < len(arr1):
        res.append(arr1[i])
        i += 1

    return sorted(res)


def main():
    list1 = list(map(lambda x: int(x), input("Введите (через пробел) элементы первого массива: ").split()))
    list2 = list(map(lambda x: int(x), input("Введите (через пробел) элементы второго массива: ").split()))
    print(define_new_array(list1, list2))


if __name__ == '__main__':
    main()
