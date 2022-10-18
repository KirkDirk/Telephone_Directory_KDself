import ui as ui
2
print('\nПривет! Чего изволите: \n')

while True:
    mode = ui.start_menu()
    if mode == 1:
        ui.out_screen_td()
    elif mode == 2:
        ui.find_contact(input('Введите имя или номер телефона (или еще что-нибудь): '))
    elif mode == 3:
        print('Здесь можно будет добавить контакт')
    elif mode == 4:
        print('Всего хорошего!')
        break
    print('\nДальше?')
