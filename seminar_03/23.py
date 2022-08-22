"""
*Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

Пример:

[2, 3, 4, 5, 6] => [12, 15, 16];
[2, 3, 5, 6] => [12, 15]
"""
# сделал по-сишному )))
def find_prod(lst):
    result = []
    begin = 0
    end = len(lst) - 1
    while (begin <= end):
        x = lst[begin] * lst[end]
        result.append(x)
        begin += 1
        end -= 1
    return result


# долго мучался с отрицательными индексами
# вот такое придумал :)
def find_prod_2(lst):
    result = []
    n = len(lst) // 2 + len(lst) % 2
    for i in range(n):
        result.append(lst[i] * lst[-(i + 1)])
    return result


if __name__ == "__main__":
    list_01 = [2, 3, 4, 5, 6]
    list_02 = [2, 3, 5, 6]

    print(find_prod(list_01))
    print(find_prod(list_02))

    print(find_prod_2(list_01))
    print(find_prod_2(list_02))
