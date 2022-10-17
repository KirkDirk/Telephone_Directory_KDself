import ui as ui

print('\nПривет! Чего изволите: \n')

while True:
    mode = ui.start_menu()
    if mode == 1:
        ui.out_screen_td()
    elif mode == 2:
        print('Здесь можно будет найти контакт')
    elif mode == 3:
        print('Здесь можно будет добавить контакт')
    elif mode == 4:
        print('Всего хорошего!')
        break
    print('\nДальше?')
