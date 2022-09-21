from operator import add, sub, mul, truediv


def operation(a: float, op: str, b: float) -> float:
    """ Считает арифметические операции для двух чисел и вернёт
        округлённый результат """
    opers = {'+': add, '-': sub, '*': mul, '/': truediv}
    callback = opers.get(op)
    if not callback:
        raise ArithmeticError('operator unknown')
    return round(callback(a, b), 2)


# вычисления
def calculate(lst: list) -> float:
    result = 0.0
    for s in lst: 
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

# разбор ввода пользователя
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


# контроллер
def run_calc(s: str):
    data = parse(s)
    result = calculate(data)
    return result