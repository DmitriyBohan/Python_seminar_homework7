from data_create import input_name, input_second_name, input_number


def input_data():
    name = input_name()
    second_name = input_second_name()
    number = input_number()
    var = int(input('В каком формате записать данные?\n\n'
                    '1\n'
                    'Владимир\n'
                    'Путин\n'
                    '89381240883\n\n'
                    '2\n'
                    'Владимир Путин :  89381240883\n\n'
                    'Выберите вариант записи: \n'))
    if var == 1:
        with open('data_first.txt', 'a', encoding='utf-8') as file:
            file.write(f'{name}\n{second_name}\n{number}\n\n')
    if var == 2:
        with open('data_second.txt', 'a', encoding='utf-8') as file:
            file.write(f'{name} {second_name} : {number}\n\n')
    print('Номер успешно сохранен')


def data_print():
    var = int(input('Телефонный справочник с каким форматом показать ?\n'
                    '1\n\n'
                    'Владимир\n'
                    'Путин\n'
                    '89381240883\n\n'
                    '2\n\n'
                    'Владимир Путин :  89381240883\n\n'
                    'Выберите вариант для показа: \n'))
    if var == 1:
        with open('data_first.txt', 'r', encoding='utf-8') as file:
            data_first = ''.join(file.readlines())
            print(data_first)
    if var == 2:
        with open('data_second.txt', 'r', encoding='utf-8') as file:
            data_second = ''.join(file.readlines())
            print(data_second)
