"""
Дана последовательность чисел. Получить отсортированный по возрастанию список уникальных элементов заданной последовательности.
Пример:
[1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]
"""

def find_unique(data: list) -> list:
    result = []
    for el in data:
        if el not in result:
            result.append(el)
        else:
            result.remove(el)
    return sorted(result)


if __name__ == "__main__":
    sequence = [1, 2, 3, 5, 1, 5, 3, 10]
    print(f'Исходная последовательность: {sequence}')
    print(f'Отсортированный список уникальных элементов: {find_unique(sequence)}')
    