"""
Задача 32: Определить индексы элементов массива (списка),
значения которых принадлежат заданному диапазону (т.е. не
меньше заданного минимума и не больше заданного
максимума)
Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
5
15
Вывод: [1, 9, 13, 14, 19]
"""
import time
array = [int(num) for num in input('Введите элементы массива (через запятую и пробел): ').split(', ')]
lower_limit = int(input('Нижняя граница диапазона: '))
upper_limit = int(input('Верхняя граница диапазона: '))
result = []

start = time.perf_counter()
for index in range(len(array)):
    if lower_limit <= array[index] <= upper_limit:
        result.append(index)
stop = time.perf_counter()
print(stop - start)

start2 = time.perf_counter()
res = [i for i in range(len(array)) if lower_limit <= array[i] <= upper_limit]
stop2 = time.perf_counter()
print(stop2 - start2)
print(result)
