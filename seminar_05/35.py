"""
В файле находится N натуральных чисел, записанных через пробел. 
Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. 
Найдите это число.
В файле data.txt записана последовательность 1 2 3 4 6 7 8 9
"""

def find_num(lst: list) -> tuple:
    for i in range(1, len(lst)):
        if lst[i] - lst[i - 1] > 1:
            return i, lst[i] - 1
    return -1, -1


if __name__ == "__main__":
    with open("data.txt", "r") as fin:
        lst = [int(i) for i in fin.readline().split()]
        print(lst)
        pos, num = find_num(lst)
        if (pos != -1):
            lst.insert(pos, num)
        print(lst)