"""
Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k),
не превосходящие числа N.
"""
n = int(input('Введите число N: '))
degree_of_two = 1
while degree_of_two <= n:
    print(degree_of_two, end=' ')
    degree_of_two *= 2
