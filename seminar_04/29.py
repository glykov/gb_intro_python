"""
Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел
"""

# НОД итеративно
def gcd(a: int, b: int) -> int:
    while b > 0:
        x = a % b
        a = b
        b = x
    return a


# НОД рекурсивно
def gcd_r(a:int, b: int) -> int:
    if b == 0:
        return a
    else:
        return gcd_r(b, a % b)


def lcm(a: int, b: int) -> int:
    return a * b // gcd(a, b)


def lcm_02(a: int, b: int) -> int:
    larger = a if a > b else b     # (a > b ? a : b)
    
    while True:
        if larger % a == 0 and larger % b == 0:
            return larger
        larger += 1    


if __name__ == "__main__":
    print(lcm(3, 4))
    print(lcm_02(3, 4))
    print(gcd(3, 7))
    print(gcd_r(3, 7))
    print(lcm(15, 4))
    print(lcm_02(15, 4))

