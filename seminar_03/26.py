"""
*Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

Пример:

для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи
"""

def fib(n: int) -> list:
    result = [0, 1]
    for i in range(2, n + 1):
        result.append(result[i - 2] + result[i - 1])
    return result


def neg_fib(lst: list) -> list:
    result = []
    for i in range(1, len(lst)):
        result.append(lst[i] * (-1) ** (i - 1))
    result = result[::-1]
    return result + lst


if __name__ == "__main__":
    print(f"{neg_fib(fib(8))}")