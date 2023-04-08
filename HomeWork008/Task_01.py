"""
Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt (.csv).
Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в текстовом файле
3. Пользователь может ввести одну из характеристик для поиска определенной записи (Например имя или фамилию
человека)
4. Использование функций. Ваша программа не должна быть линейной
"""
import csv


def show_menu():
    print('Введите число для операции со справочником:')
    print('1 - вывести весь справочник;\n2 - найти абонента по фамилии;\n'
          '3 - найти абонента по номеру телефона;\n4 - ввести данные нового абонента;\n'
          '5 - удалить данные абонента;\n6 - изменить данные абонента\n'
          '7 - завершить работу.')


def print_user_info(row):
    print(f'Фамилия: {row[0]}\nимя: {row[1]}\nномер телефона: {row[2]}\nкомментарий: {row[3]}\n')


def display_all_records():
    with open('phonebook.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            print_user_info(row)


def find_last_name(last_name):
    with open('phonebook.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        result = list(filter(lambda x: x[0] == last_name, reader))
        if len(result) > 0:
            for row in result:
                print_user_info(row)
        else:
            print(f'Абонент с фамилией "{last_name}" не найден.\n')


def find_phone_number(phone_number):
    with open('phonebook.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        result = list(filter(lambda x: x[2] == phone_number, reader))
        if len(result) > 0:
            for row in result:
                print_user_info(row)
        else:
            print(f'Абонент с номером {phone} не найден.\n')


def add_user(info):
    with open('phonebook.csv', 'a', encoding='utf-8', newline='') as file:
        csv.writer(file).writerow(info)


def del_user_info(info):
    with open('phonebook.csv', 'r+', encoding='utf-8') as file:
        data = list(csv.reader(file))
        user_data = list(filter(lambda x: x[0] == info[0] and x[2] == info[1], data))
        if len(user_data) > 0:
            data.remove(user_data[0])
            file.seek(0)
            csv.writer(file).writerows(data)
            file.truncate()
            return True
        else:
            print(f'Пользователь с фамилией "{info[0]}" и телефоном {info[1]} не найден.\n')
            return False


def change_user_info(info):
    with open('phonebook.csv', 'r+', encoding='utf-8') as file:

        data = list(csv.reader(file))
        user_data = list(filter(lambda x: x[0] == info[0] and x[2] == info[1], data))
        if len(user_data) > 0:
            del_user_info(info)
            print('Вы пытаетесь обновить данные пользователя:')
            print_user_info(*user_data)
            new_user_info = input('Обновленные данные пользователя '
                                  '(Фамилия, имя, телефон и комментарий через запятую): ').split(', ')
            add_user(new_user_info)
            print('Данные пользователя изменены.\n')
        else:
            print(f'Пользователь с фамилией "{info[0]}" и телефоном {info[1]} не найден.\n')


show_menu()

for number in iter(input, '7'):

    if number == '1':
        display_all_records()

    elif number == '2':
        name = input('Введите фамилию: ')
        find_last_name(name)

    elif number == '3':
        phone = input('Введите номер телефона: ')
        find_phone_number(phone)

    elif number == '4':
        user_info = input('Введите данные абонента (фамилия, имя, номер, комментарий - через запятую): ').split(', ')
        add_user(user_info)
        print(f'Данные абонента "{user_info[1]} {user_info[0]}" записаны.\n')

    elif number == '5':
        user_info = input('Введите фамилию и номер телефона абонента для удаления (через запятую): ').split(', ')
        if del_user_info(user_info):
            print(f'Пользователь с фамилией "{user_info[0]}" и телефоном {user_info[1]} удален.\n')

    elif number == '6':
        user_info = input('Введите фамилию и номер телефона абонента для изменения данных (через запятую): ').split(', ')
        change_user_info(user_info)

    show_menu()

else:
    print('Работа завершена.')
