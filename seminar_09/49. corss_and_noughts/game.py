"""
Создайте программу для игры в "Крестики-нолики".
"""
import random

chip = {'cross': 'X', 'nought': 'O', 'empty': '_'}


def init_field() -> list:
    return [[chip['empty'] for col in range(3)] for row in range(3)]


def print_field(field: list):
    for row in range(len(field)):
        print('| ', end='')
        for col in range(len(field[row])):
            print(field[row][col], end=' | ')
        print()
        for col in range(len(field[row])):
            print('+---', end='')
        print('+')


def is_valid_cell(row: int, col: int) -> bool:
    return 0 <= row <= 2 and 0 <= col <= 2


def is_empty_cell(field: list, row: int, col: int) -> bool:
    return field[row][col] == chip['empty']


def player_turn(field: list):
    row, col = 0, 0
    while True:
        row = int(input("Введите строку от 1 до 3: ")) - 1
        col = int(input("Введите столбец от 1 до 3: ")) - 1
        if is_valid_cell(row, col) and is_empty_cell(field, row, col):
            break
    field[row][col] = chip['cross']


def ai_turn(field: list):
    row, col = 0, 0
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if is_empty_cell(field, row, col):
            break
    field[row][col] = chip['nought']


def is_field_full(field: list) -> bool:
    for row in range(3):
        for col in range(3):
            if field[row][col] == chip['empty']:
                return False
    return True


def check_for_winner(field: list, symbol: str) -> bool:
    return check_horizontal(field, symbol) or check_vertical(field, symbol) or check_diagonal(field, symbol)


def check_horizontal(field: list, symbol: str) -> bool:
    for row in range(3):
        counter = 0
        for col in range(3):
            if field[row][col] == symbol:
                counter += 1
        if counter == 3:
            return True
    return False


def check_vertical(field: list, symbol: str) -> bool:
    for i in range(3):
        counter = 0
        for j in range(3):
            if field[j][i] == symbol:
                counter += 1
        if counter == 3:
            return True
    return False


def check_diagonal(field: list, symbol: str) -> bool:
    main = 0
    side = 0
    for i in range(3):
        if field[i][i] == symbol:
            main += 1
        if field[i][2 - i] == symbol:
            side += 1
    if main == 3 or side == 3:
        return True
    return False


def play_one_round():
    rows = 3
    cols = 3
    field = init_field()
    print_field(field)

    while True:
        print('--------- ХОД ИГРОКА --------')
        player_turn(field)
        print_field(field)
        if check_for_winner(field, chip['cross']):
            print('Игрок победил!')
            break
        if is_field_full(field):
            print('Ничья!')
            break
        print('--------- ХОД КОМПЬЮТЕРА ---------')
        ai_turn(field)
        print_field(field)
        if check_for_winner(field, chip['nought']):
            print('Электронный болван победил')
            break
        if is_field_full(field):
            print('Ничья!')
            break


if __name__ == "__main__":
    while True:
        play_one_round()
        choice = input('Хотите сыграть еще (Д/Н)? ')
        if choice.lower() != 'д':
            break
