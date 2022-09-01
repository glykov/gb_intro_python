"""
Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
a) Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
 Например, число `19 ^ 3 = 6859` будем включать в сумму, так как `6 + 8 + 5 + 9 = 28` – делится нацело на `7`. 
Внимание: использовать только арифметические операции!
b) К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
"""

def make_list(n: int) -> list:
    # list comprehension + filter + lambda
    return [i ** 3 for i in filter(lambda x: x % 2, range(1, n + 1))]


def sum_of_digits(number: int) -> int:
    result = 0
    while (number > 0):
        result += number % 10
        number //= 10
    return result

def calc_sum(divisor: int, data: list) -> int:
    # filter + sum + lambda
    return sum(filter(lambda x: sum_of_digits(x) % divisor == 0, data))


def update_list(data: list, value: int) -> list:
    return list(map(lambda x: x + value, data))


if __name__ == "__main__":
    numbers = make_list(1000)
    # print(f'Исходная последовательность: {numbers}')
    n1 = calc_sum(7, numbers)
    print(n1)                       # 17485588610 - как и в прошлый раз, ура!!!
    numbers_17 = update_list(numbers, 17)
    n2 = calc_sum(7, numbers_17)    # 15392909930 - снова совпало :)
    print(n2)
    