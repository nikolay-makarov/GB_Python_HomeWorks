"""
Проверка палиндрома. Напишите функцию, которая проверяет,
является ли строка палиндромом (то есть читается одинаково справа налево и слева направо)
с использованием рекурсии.
"""


def is_palindrome(string, index=0):
    if index <= len(string) // 2:
        if string[index] != string[len(string) - 1 - index]:
            return 'Не палиндром'
        is_palindrome(string, index + 1)
    return 'Палиндром'


print(is_palindrome('12321'))  # Палиндром
print(is_palindrome('123456'))  # Не палиндром
