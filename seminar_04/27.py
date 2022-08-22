"""
Задайте строку из набора чисел.
 Напишите программу, которая покажет большее и меньшее число. 
 В качестве символа-разделителя используйте пробел.
"""

def min_max(lst: list) -> tuple:
    maximum = lst[0]
    minimum = lst[0]

    for el in lst:
        if el > maximum:
            maximum = el
        if el < minimum:
            minimum = el
    
    return maximum, minimum


if __name__ == "__main__":
    numbers = [int(i) for i in "1 23 4 -15 90 88 -23 777 -3".split()]
    maximum, minimum = min_max(numbers)
    print(f"максимум = {maximum}, минимум = {minimum}")
