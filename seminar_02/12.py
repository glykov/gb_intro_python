"""
Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.

Пример:

Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
"""
def calculate(n: int) -> int:
    return 3 * n + 1
my_map = {}

if __name__ == "__main__":
    x = int(input("Введите количество значений: "))

    for i in range(1, x + 1):
        my_map[i] = calculate(i)

    print(my_map)
