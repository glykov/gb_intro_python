"""
Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.

Примеры:

5, 25 -> да
4, 16 -> да
25, 5 -> да
8,9 -> нет
"""
x, y = map(int, input().split(','))
if (x ** 2 == y or y ** 2 == x):
    print("YES")
else:
    print("NO")