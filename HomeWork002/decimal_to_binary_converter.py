"""
Напишите программу, которая будет преобразовывать десятичное число в двоичное.
*Пример:*
- 45 -> 101101
- 3 -> 11
- 2 -> 10
"""
number = int(input('Введите число: '))
result = ''
remainder = number
while remainder > 0:
    result += str(remainder % 2)
    remainder //= 2
print(f'{number} -> {result[::-1]}')
