"""
*Напишите программу, которая будет преобразовывать десятичное число в двоичное.

Пример:

45 -> 101101
3 -> 11
2 -> 10
"""

def int_to_bin(n: int) -> str:
    result = ""
    while (n > 0):
        result += "1" if n % 2 == 1 else "0"
        n //= 2
    return "".join(reversed(result))


if __name__ == "__main__":
    a, b, c = 45, 3, 2
    print(f"{a} -> {int_to_bin(a)}")
    print(f"{b} -> {int_to_bin(b)}")
    print(f"{c} -> {int_to_bin(c)}")