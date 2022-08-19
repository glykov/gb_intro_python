"""
Задайте список из n чисел последовательности (1 + 1 / n) ** n
 
 и выведите на экран их сумму.

Пример:

Для n = 6:
"""

def calculate(n: int) -> float:
    return (1 + 1 / n) ** n

if __name__ == "__main__":
    x = int(input("Введите количество элементов последовательности: "))
    lst = []
    for i in range(1, x + 1):
        lst.append(calculate(i))
    
    print(round(sum(lst), 2))