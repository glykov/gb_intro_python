"""
Создайте программу для игры с конфетами человек против человека.

Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
Все конфеты оппонента достаются сделавшему последний ход. 
Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

a) Добавьте игру против бота

b) Подумайте как наделить бота "интеллектом"
"""
import random

total_candies = 2021
move = 1
gamer = 2
while total_candies > 0:
    gamer = 1 if gamer == 2 else 2
    print(f'Раунд {move}:')
    move += 1
    message = f"Игрок {gamer}: "
    if gamer == 1:
        number_of_candies = int(input(f"{message}Сколько конфет вы возьмете (1 - 28)? "))
        while(number_of_candies < 1 or number_of_candies > 28):
            print(f'{message} взял неправильное количество конфет, попробуйте снова')
            number_of_candies = int(input(f"{message}Сколько конфет вы возьмете (1 - 28)? "))
    else:
        number_of_candies = random.randint(1, 28)   # не придумал как как наделить бота "интеллектом"
    print(f'{message}взял {number_of_candies} конфет')
    total_candies -= number_of_candies
    print(f'Осталось {total_candies} конфет')

print(f'Выиграл игрок {gamer}')