"""
Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
Найдите произведение элементов на указанных позициях. 
Позиций может быть более двух, пользователь вводит индексы с клавиатуры.
"""
import random

n = int(input("Введите количество элементов: "))

lst = []
for i in range(n):
    lst.append(random.randint(-n, n))

sum = 0
while (True):
    index = int(input(f"Введите интдекс элемента для суммирования (0, {n}),\nили -1 для прекращения ввода: "))
    if index < 0:
        break
    sum += lst[index]

print(f"Сумма указанных элементов = {sum}")