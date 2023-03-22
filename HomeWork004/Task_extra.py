"""
Создайте программу для игры с конфетами человек против человека.
Условие задачи: На столе лежит 2021 конфета.
Играют два игрока делая ход друг после друга.
Первый ход определяется жеребьёвкой.
За один ход можно забрать не более чем 28 конфет.
Все конфеты оппонента достаются сделавшему последний ход.
Сколько конфет нужно взять первому игроку,
чтобы забрать все конфеты у своего конкурента?
"""
from random import randint

candies_on_table = int(input('Сколько конфет лежит на столе? '))
current_player = randint(0, 1)  # Определяем, кто ходит первым: 0 - PC, 1 - Пользователь

while candies_on_table > 0:

    if current_player == 1:  # Пользователь
        print(f'Ход делает Пользователь.')
        can_take = 28 if candies_on_table > 28 else candies_on_table  # Максимальное число конфет, которое можно взять
        recommend_number = candies_on_table % 29 if candies_on_table % 29 != 0 else randint(1, 28)
        print(f'На столе {candies_on_table} конфет. (Рекомендуем взять {recommend_number} конфет.)')
        take_candies = int(input(f'Сколько конфет нужно взять? (введите число от 1 до {can_take}) '))
        while take_candies < 1 or take_candies > 28 or take_candies > candies_on_table:
            take_candies = int(input('Вы пытаетесь взять неверное количество конфет! Попробуйте снова: '))
        candies_on_table -= take_candies
        print(f'Пользователь взял {take_candies} конфет, осталось {candies_on_table} конфет.')

        if candies_on_table == 0:
            print('Победил Пользователь!')

        current_player = 0  # Переход хода
        print()

    elif current_player == 0:  # Компьютер
        print(f'Ход делает PC.')
        print(f'На столе {candies_on_table} конфет.')
        take_candies = candies_on_table % 29 if candies_on_table % 29 != 0 else randint(1, 28)
        candies_on_table -= take_candies
        print(f'PC взял {take_candies} конфет, осталось {candies_on_table} конфет.')

        if candies_on_table == 0:
            print(f'Победил PC!')

        current_player = 1
        print()

print('Игра закончена!')
