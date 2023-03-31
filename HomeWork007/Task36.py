"""
Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
"""


def print_operation_table(operation, num_rows=6, num_columns=6):
    """Функция в форматированном виде распечатывает номера столбцов, строк и на их пересечении
    результат применения функции, переданной в параметре operation."""
    # Выводим на экран номера столбцов:
    for col in range(num_columns + 1):
        print(str(col).ljust(3), end=' ')
    print()
    print('----' * (num_columns + 1))

    for i in range(1, num_rows + 1):
        # Выводим на экран номера строк:
        print(f'{str(i).ljust(2)}|', end=' ')

        # Выводим на экран результат вычисления функции по номеру строки и столбца:
        for j in range(1, num_columns + 1):
            print(str(operation(i, j)).ljust(3), end=' ')
        print()


print_operation_table(lambda x, y: x * y, 5, 5)
print()
print_operation_table(lambda x, y: x + y, 7, 7)
