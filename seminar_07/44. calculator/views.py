# получение данных от пользователя - view
def get_rational() -> str:
    return input("Введите выражение (например: 6/10+1.5): ")


def get_complex() -> list:
    result = []
    a = float(input("Введите вещественную часть первого числа: "))
    b = float(input("Введите мнимую часть первого числа: "))
    op = input("Введите операцию: ")
    c = float(input("Введите вещественную часть второго числа: "))
    d = float(input("Введите мнимую часть второго числа: "))
    return [[a, b], op, [c, d]]


# выбор типа чисел для работы  -> view
def show_menu() -> str:
    result = input("Выберите тип чисел для работы (Q - рациональные, C - комплексные): ")
    return result.upper()


# вывод результата
def show_result(result: float):
    print(f'Результат вычислений {result:.2f}')

# вывод результата для комплексного числа
def show_result_c(result: tuple):
    print(f'Результат вычислений ({result[0]:.2f} {result[1]:+.2f})')
