"""
Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
*Пример:*
3 2 4 -> yes
3 2 1 -> no
"""
length = int(input('Введите длину шоколадки (в дольках): '))
width = int(input('Введите ширину шоколадки (в дольках): '))
amount = int(input('Сколько долек нужно отломить? '))

if length * width > amount and (not amount % length or not amount % width):
    # Считаем, что число долек, которые нужно отломить, должно быть меньше общего количества долек
    answer = 'можно'
else:
    answer = 'нельзя'

print(f'От шоколадки размером {length} * {width} долек {answer} отломить {amount} долек.')