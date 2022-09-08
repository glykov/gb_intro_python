from argparse import ArgumentError
from operator import add, sub, mul, truediv


def operation(a: float, op: str, b: float) -> float:
    """ Считает арифметические операции для двух чисел и вернёт
        округлённый результат """
    opers = {'+': add, '-': sub, '*': mul, '/': truediv}
    callback = opers.get(op)
    if not callback:
        raise ArithmeticError('operator unknown')
    return round(callback(a, b), 2)


# разбор ввода пользователя
def calculate(lst: list) -> float:
    result = 0.0
    for s in lst:  # пришлось разделить вычисления */ и +- и идти последовательно по списку теперь производит корректное вычисление '6/10*10-10'
        if s == '*' or s == '/':
            index = lst.index(s)
            result = operation(lst[index - 1], s,  lst[index + 1])
            lst = lst[:index - 1] + [result] + lst[index + 2:]
    for s in lst: 
        if s == '+' or s == '-':
            index = lst.index(s)
            result = operation(lst[index - 1], s,  lst[index + 1])
            lst = lst[:index - 1] + [result] + lst[index + 2:]
    return result

    
def parse(s: str) -> list:
    result = []
    digit = ""
    for symbol in s:
        if symbol.isdigit() or symbol == '.':
            digit += symbol
        elif symbol in ['(', ')']:
            if digit:
                result.append(float(digit))
                digit = ""
            result.append(symbol)
        else:
            if digit:
                result.append(float(digit))
            digit = ""
            result.append(symbol)
    else:
        if digit:
            result.append(float(digit))
    return result


def mul(a: list, b:list) -> list:
    r = a[0] * b[0] - a[1] * b[1]
    i = a[1] * b[0] + a[0] * b[1]
    return [r, i]


def div(a: list, b:list) -> list:
    d = b[0] ** 2 + b[1] ** 2
    r = (a[0] * b[0] + a[1] * b[1]) / d
    i = (a[1] * b[0] - a[0] * b[1]) / d
    return [r, i]


def add(a: list, b:list) -> list:
    return [a[0] + b[0], a[1] + b[1]]


def sub(a: list, b:list) -> list:
    return [a[0] - b[0], a[1] - b[1]]


def calculate_c(data: list) -> list:
    if data[1] == '*':
        return mul(data[0], data[2])
    elif data[1] == '/':
        return div(data[0], data[2])
    elif data[1] == '+':
        return add(data[0], data[2])
    elif data[1] == '-':
        return sub(data[0], data[2])
    else:
        raise ArgumentError("Illegal operation passed")
    