"""
*Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

Пример:

[1.1, 1.2, 3.1, 5, 10.01] => 0.19
"""
flist = [1.1, 1.2, 3.1, 5, 10.01]
min_fract = 0.0
max_fract = 0.0
is_first_pass = True
for el in flist:
    x = el - int(el)
    if is_first_pass:
        min_fract = max_fract = x
        is_first_pass = False
    elif x < min_fract:
        min_fract = x
    elif x > max_fract:
        max_fract = x

# print(f"{(max_fract - min_fract):.2f}") - округляет и выводит 0.20 
# print(max_fract - min_fract) - выводит 0.19999999996
# поэтому сделал так
print(str(max_fract - min_fract)[:4])