def out_new_persona(persona):
    with open('db.txt', 'a') as db_write:
        db_write.write(persona + '\n')