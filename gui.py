from logger import input_data, data_print


def interface():
    print('Выбирете действие:\n'
          '1  Добавить новый номер\n'
          '2  Посмотреть справочник\n')
    var = int(input('Введите номер: '))
    if var == 1:
        input_data()
    if var == 2:
        data_print()
