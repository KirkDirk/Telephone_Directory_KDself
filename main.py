import ui as ui

print('Привет! Чего изволите: \n')
mp = ui.start_menu()
if mp == 1:
    ui.out_screen_td()
    print('\nДальше?')
    ui.start_menu()
elif mp == 2:
    print('Здесь можно будет найти контакт')
elif mp == 3:
    print('Здесь можно будет добавить контакт')
elif mp == 4:
    print('Всего хорошего!')
    exit

