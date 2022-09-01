"""
Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный.
Пример:
2+2 => 4;
1+2*3 => 7;
1-2*3 => -5;
Добавьте возможность использования скобок, меняющих приоритет операций.
Пример:
1+2*3 => 7;
(1+2)*3 => 9;
"""

def parse(s: str) -> list:
    result = []
    digit = ""
    for symbol in s:
        if symbol.isdigit():
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


def calculate(lst: list) -> float:
    result = 0.0
    while '*' in lst:
        index = lst.index('*')
        result = lst[index - 1] * lst[index + 1]
        lst = lst[:index - 1] + [result] + lst[index + 2:]
    while '/' in lst:
        index = lst.index('/')
        result = lst[index - 1] / lst[index + 1]
        lst = lst[:index - 1] + [result] + lst[index + 2:]
    while '+' in lst:
        index = lst.index('+')
        result = lst[index - 1] + lst[index + 1]
        lst = lst[:index - 1] + [result] + lst[index + 2:]
    while '-' in lst:
        index = lst.index('-')
        result = lst[index - 1] - lst[index + 1]
        lst = lst[:index - 1] + [result] + lst[index + 2:]
    return result


def brackets(lst:list) -> list:
    while '(' in lst:
        opening = lst.index('(')
        closing = lst.index(')')
        lst = lst[:opening] + [calculate(lst[opening + 1:closing])] + lst[closing + 1:]
    return lst

if __name__ == "__main__":
    s = "(1+1)+20+2*50-2/2+(5+5)+10-(1+1)"
    result = parse(s)
    print(result)
    result = brackets(result)
    print(result)
    print(calculate(result))

