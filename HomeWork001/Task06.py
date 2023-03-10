"""
Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
Вам требуется написать программу, которая проверяет счастливость билета.
*Пример:*
385916 -> yes
123456 -> no
"""
ticket_number_string = input('Введите номер билета из 6 цифр: ')

if ticket_number_string.isdigit() and len(ticket_number_string) == 6:
    first_part = ticket_number_string[:3]
    last_part = ticket_number_string[3:]
    first_digits_sum = int(first_part[0]) + int(first_part[1]) + int(first_part[2])
    last_digits_sum = int(last_part[0]) + int(last_part[1]) + int(last_part[2])
    answer = ['не является', 'является'][first_digits_sum == last_digits_sum]
    print(f'Билет {ticket_number_string} {answer} счастливым.')
else:
    print('Введенные данные не соответствуют условию задачи!')
