"""
Задача 18: Требуется найти в массиве A[1..N] самый близкий по
величине элемент к заданному числу X. Пользователь в первой строке
вводит натуральное число N – количество элементов в массиве. В
последующих строках записаны N целых чисел A. Последняя строка
содержит число X
"""

# Решение позволяет найти несколько элементов массива, которые по значению одинаково близки к искомому числу X.
# Для этого создается список result_numbers_list, куда записываются числа, удовлетворяющие условию.
# Например, числа 2 и 4 одинаково близки числу 3, поэтому попадают в результат

n = int(input('Введите число элементов массива: '))
print('Введите элементы массива: ')
array = [int(input()) for _ in range(n)]
x = int(input('Введите число X: '))

result = array[0]
result_numbers_list = list()
result_numbers_list.append(str(result))  # В список записывается числа в виде строк,
# чтобы удобнее было вывести результат используя метод join.
min_difference = abs(x - array[0])

for number in array[1:]:
    if abs(number - x) < min_difference:
        result = number
        min_difference = abs(number - x)
        result_numbers_list.clear()
        result_numbers_list.append(str(result))
    elif abs(number - x) == min_difference:
        result_numbers_list.append(str(number))

print(f'К числу {x} наиболее близки элементы массива со значениями: {", ".join(set(result_numbers_list))}.')
