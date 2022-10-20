import read as dataread
import append as dataappend
import csv

def start_menu():
    mode_program = int(input(
        '1. Печатать весь телефонный справочник \n'
        '2. Найти контакт \n'
        '3. Добавить контакт \n'
        '4. Давай, до свидания \n'
        ':'
        ))
    while mode_program not in (1, 2, 3, 4):
        int(input('Ошибка, введите число от 1 до 4'))
    return mode_program

def out_menu():
    mode_out = int(input(
        '1. Вывести на экран \n'
        '2. Вывести в .csv \n'
        ':'
        ))
    while mode_out not in (1, 2):
        int(input('Ошибка, введите число от 1 до 2'))
    if mode_out == 1:
        out_screen_td()
    else:
        out_csv()
    return 

def out_screen_td():
    tel_dir_data = dataread.get_all_data()
    name_column = ['id', 'Фамилия', 'Имя', 'Отчество', 'Телефон', 'Примечание']
    for line in tel_dir_data:
        temp_str = line.split('::')
        for i in range(len(temp_str)):
            if temp_str[i] != '-1':
                print(name_column[i], temp_str[i]+'  ', sep = ': ', end = ' ')

def out_csv():
    tel_dir_data = dataread.get_all_data()
    column_csv = '''Фамилия, Имя, Отчество, Телефон, Примечание\n'''
    with open('db.csv', 'a', encoding='utf-8') as out:
        out.write(column_csv)    
        for line in tel_dir_data:
            temp_str = line.split('::')
            del temp_str[0]
            out.write(','.join(temp_str))
    return
            
def find_contact(find_data):
    tel_dir_data = dataread.get_all_data()
    found_list = []
    for line in tel_dir_data:
        if find_data in line:
            found_list.append(line)
    if found_list>[]:
        for elem in found_list:
            print(elem, end = '')
    else: print('Искомое не найдено')
    return
        
