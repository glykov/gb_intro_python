"""
Создайте программу для игры с конфетами человек против человека.
Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
Все конфеты оппонента достаются сделавшему последний ход. 
Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
a) Добавьте игру против бота
b) Подумайте как наделить бота "интеллектом" - Бот меня обыграл - Восстание машин (((
"""
import random

def player_turn(candies: int) -> int:
    number_of_candies = int(input("Сколько конфет вы возьмете (1 - 28)? "))
    while(number_of_candies < 1 or number_of_candies > 28):
        print("Вы взяли неправильное количество конфет, попробуйте снова")
        number_of_candies = int(input("Сколько конфет вы возьмете (1 - 28)? "))
    return candies - number_of_candies


def bot_turn(candies: int) -> int:
    while True:
        taken_candies = random.randint(1, 28)
        if (candies - taken_candies) % 29 == 0:
            print(f'Бот взял {taken_candies} конфет')
            return candies - taken_candies


if __name__ == "__main__":
    total_candies = 2021
    move = 1
    gamer = "Игрок"
    while total_candies > 0:
        gamer = "Игрок" if move % 2 == 1 else "Бот"
        print(f'Раунд {move}:')
        move += 1
        message = f"Игрок {gamer}: "
        if gamer == "Игрок":
            total_candies = player_turn(total_candies)
        else:
            total_candies = bot_turn(total_candies)

        print(f'Осталось {total_candies} конфет')

    print(f'Выиграл {gamer}') 