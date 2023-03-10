"""
Задача 2: Найдите сумму цифр трехзначного числа.
*Пример:*
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0)
"""
number = int(input('Введите трехзначное число: '))

if 100 <= number <= 999:
    ones = number % 10
    tens = number // 10 % 10
    hundreds = number // 100
    result = ones + tens + hundreds
    print(f'Сумма цифр числа {number} -> {result} ({hundreds} + {tens} + {ones})')
else:
    print('Введенное число не является трехзначным!')
