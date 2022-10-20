def get_all_data():
    with open('db.txt', 'r', encoding='utf-8') as dbread:
        td_data = dbread.readlines()
    return td_data

def get_last_id():
    with open('db.txt', 'rb') as dbread:
        dbread.seek(-300, 2)
        last_str = dbread.readlines()[-1].decode('utf-8')
        last_id = ''
        for char in last_str:
            if char != ':':
                last_id += char
            else: break
    return last_id