"""
Реализуйте алгоритм перемешивания списка. (не использовать из модуля random метод shuffle другие методы допускается)
"""

import random

lst = [random.randint(0, 100) for i in range(10)]
print(f"Исходный список: {lst}")

for i in range(len(lst)):
    a = random.randint(0, len(lst) - 1)
    b = random.randint(0, len(lst) - 1)
    if a != b:
        lst[a], lst[b] = lst[b], lst[a]

print(f"Измененный список: {lst}")