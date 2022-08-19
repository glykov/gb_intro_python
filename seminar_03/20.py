"""
Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
"""

strings = ["1", "another string", "string 3", "hello world", "123"]

num_to_search = input("Введите число для поиска: ")
found = False

for s in strings:
    if num_to_search in s:
        found = True
        break

print("Число найдено" if found else "Число не найдено")
