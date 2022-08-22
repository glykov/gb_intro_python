"""
Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.
"""
import random
import time

x = random.randint(1, 100)

def get_rand(x: int, y: int) -> int:
    if x > y:
        raise ValueError("Ошибка! x должен быть меньше у")
    scope = y - x    
    result = int(time.time()) % scope
    return result + x
    


if __name__ == "__main__":
    print(get_rand(80, 100))
