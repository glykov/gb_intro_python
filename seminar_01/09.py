"""
*Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
"""

quarter = int(input("Введите номер чтеверти (0-4): "))

if (quarter == 1):
    print("x(0, +inf) y(0, + inf)")
elif (quarter == 2):
    print("x(-inf, 0) y(0, + inf)")
elif (quarter == 3):
    print("x(-inf, 0) y(-inf, 0)")
elif (quarter == 4):
    print("x(0, +inf) y(-inf, 0)")
else:
    print("Номер четверти должен быть от 1 до 4, Вы ввели ", quarter)