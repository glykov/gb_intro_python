"""
Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N

Примеры:

5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5
"""

n = int(input("Enter a number: "))

i = -n

while (i <= n):
    print(i, end=(', ' if i != n else ''))
    i += 1

print()