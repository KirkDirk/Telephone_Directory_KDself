import read as dataread

def add_new_personage():
    personage = str(int(dataread.get_last_id())+1)
    while len(personage)<7:
        personage = '0'*(7-len(personage)) + personage
    name_column = ['фамилия', 'имя', 'отчество', 'телефон', 'комментарий']
    for i in range(0, 5):
        personage += '::'
        temp_date = input('Введите: ' + name_column[i] + ': ')
        if temp_date == '': 
            temp_date = '-1'        
        personage += temp_date
    with open('db.txt', 'a', encoding='utf-8') as db_write:
        db_write.write('\n' + personage)