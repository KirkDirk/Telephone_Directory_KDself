import read as dataread
import append as dataappend

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

def out_screen_td():
    tel_dir_data = dataread.get_all_data()
    name_column = ['id', 'Фамилия', 'Имя', 'Отчество', 'Телефон', 'Примечание']
    print('   ', end = '')
    for line in tel_dir_data:
        temp_str = line.split('::')
        for i in range(len(temp_str)):
            if temp_str[i] != '-1':
                print(name_column[i], temp_str[i]+'  ', sep = ': ', end = ' ')
            
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
        
