def get_all_data():
    with open('db.txt', 'r', encoding='utf-8') as dbread:
        td_data = dbread.readlines()
        for line in td_data:
            line[len(line)-1].rstrip
    return td_data
