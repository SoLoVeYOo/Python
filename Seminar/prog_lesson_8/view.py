def return_find_result(familiya, tel):
    print(f'{familiya}, номер телефона в записной книжке: {tel}')

def new_contakt():
    contakt = [i for i in input('Введите данные "фамилия" "имя" "телефон" (без ковычек),'
    '\nкоторые хотите добавить через запятую'
    '\n(для выхода в предыдущее меню введите "q" без ковычек).'
    '\nВвод: ').split(',')]
    return contakt

def find_phone():
    poisk = input('Введите фамилию для поиска (для выхода в предыдущее меню введите "q" без ковычек): ')
    return poisk