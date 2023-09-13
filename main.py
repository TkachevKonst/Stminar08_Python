# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной
# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и
# Вы должны реализовать функционал для изменения и удаления данных


def read_all(data):
    with open(data, 'r', encoding='UTF8') as dt:
        print(dt.read().strip())

def write_new(data):
    new_str1 = input('Фамилия: ')
    new_str2 = input('Имя: ')
    new_str3 = input('Телефон: ')
    new_str = new_str1 + ', ' + new_str2 + ', ' + new_str3
    with open(data, 'a', encoding='utf8') as dt:
        dt.write(new_str+'\n')

def find_item(data):
    text_item = input('Параметр: ')
    with open(data, 'r', encoding='UTF8') as dt:
        for line in dt:
            if text_item.lower() in line.lower():
                print(line)

def find_item_2(data):
    item = input('Что ищем: ')
    item_type = int(input('Введите номер (1-фамилия, 2-имя, 3-телефон): '))
    with open(data, 'r', encoding='utf8') as dt:
        for line in dt:
            line = line.split(', ')
            if item.lower() in line[item_type-1].lower():
                print(*line)

def sort_list2(data):
    lst = list()
    item_type = int(input('Введите номер (1-фамилия, 2-имя, 3-телефон): '))
    with open(data, 'r', encoding='UTF8') as dt:
        for line in dt:
            line = line.split(', ')
            lst.append(line)
        lst.sort(key=lambda person: person[item_type-1])
    with open(data, 'w', encoding='UTF8') as dt:
        for line in lst:
            line = ', '.join(line)
            dt.write(line)

def sort_list(data):
    lst = list()
    with open(data, 'r', encoding='UTF8') as dt:
        for line in dt:
            lst.append(line)
            lst.sort()
    with open(data, 'w', encoding='UTF8') as dt:
        for line in lst:
            dt.write(line)

def delete_telefon(data):
    lst = list()
    item = input('Какой контакт удалить: ')
    with open(data, 'r', encoding='utf8') as dt:
        for line in dt:
            if item.lower() in line.lower():
                line = ''
            lst.append(line)
            lst.sort()
    with open(data, 'w', encoding='UTF8') as dt:
        for line in lst:
            dt.write(line)


def change_contact (data):
    lst = list()
    item = input('Какой контакт изменить: ')
    item_type = int(input('Введите номер что хотите изменить (1-фамилия, 2-имя, 3-телефон): '))
    with open(data, 'r', encoding='utf8') as dt:
        for line in dt:
            if item.lower() in line.lower():
                line = line.split(', ')
                line[item_type-1] = input('Введите изменение: ')
                line = ', '.join(line)
            lst.append(line)
            lst.sort()
    with open(data, 'w', encoding='UTF8') as dt:
        for line in lst:
            dt.write(line)



def main(data):
    print('Введите номер операции, где: ',
                '1-поиск',
                '2-создание нового контакта',
                '3-вывод всей телефонной книги',
                '4-сортировка по параметрам',
                '5-удаление контакта',
                '6 - изменение контакта',
                '0 - выход : ', sep='\n', end='\n')
    match input():
        case '1':
            find_item_2(data)
        case '2':
            write_new(data)
        case '3':
            read_all(data)
        case '4':
            sort_list2(data)
        case '5':
            delete_telefon(data)
        case '6':
            change_contact(data)
        case '0':
            print('Good bay!!!')





tl = 'Telefon.txt'
main(tl)


