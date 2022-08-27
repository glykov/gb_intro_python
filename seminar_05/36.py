"""
Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность. Порядок элементов менять нельзя.
Пример:
[1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.
"""

def check(seq: list) -> bool:
    n = len(seq)
    if n < 2:
        return False
    for i in range(1, n):
        if seq[i - 1] >= seq[i]:
            return False
    return True


def generate(lst: list) -> list:
    width = len(lst)
    n = 2 ** width
    result = []

    for i in range(n):
        temp = []
        for j in range(width):
            if (i & (1 << j)):
                temp.append(lst[j])
        if (check(temp)):
            result.append(temp)
    return result


if __name__ == "__main__":
    lst = [1, 5, 2, 3, 4, 6, 1, 7]
    

    for el in generate(lst):
        print(el)
