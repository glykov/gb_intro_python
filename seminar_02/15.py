"""
Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

Пример:

пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 12, 123, 1234)
"""

def calculate(n: int) -> int:
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


if __name__ == "__main__":
    n = int(input("Введите необходимое количество элементов: "))
    lst = []
    for i in range(n):
        lst.append(calculate(i + 1))

    print(lst) 