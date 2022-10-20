import ui as ui
import append as append

print('\nПривет! Чего изволите: \n')

while True:
    mode = ui.start_menu()
    if mode == 1:
        ui.out_menu()
    elif mode == 2:
        ui.find_contact(input('Введите имя или номер телефона (или еще что-нибудь): '))
    elif mode == 3:
        append.add_new_personage()
    elif mode == 4:
        print('Всего хорошего!')
        break
    print('\nДальше?')
