"""
Сгенерировать файл из чисел в диапазоне [-2, 2], используя утилиту utils/gen_4_30.py. 
Написать программу, считывающую все значения чисел из сгенерированного файла и выводящую в stdout только уникальные значения.
"""

def make_unique(filename: str) -> set:
    result = []
    with open(filename, 'r') as fin:
        for s in fin:
            x, y = map(int, s.split())
            result.append(x)
            result.append(y)
    return set(result)


if __name__ == "__main__":
    values = make_unique('data_4_31.txt')
    for value in values:
        print(value)