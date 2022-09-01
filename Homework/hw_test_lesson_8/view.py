def return_find_result(zapros, resultat): # отредактировано
    print(f'{zapros}, вывод результата по заданному запросу: {resultat}')

def new_contakt():
    contakt = [i for i in input('Введите данные "фамилия" "имя" "телефон" (без ковычек),'
    '\nкоторые хотите добавить через запятую'
    '\n(для выхода в предыдущее меню введите "q" без ковычек).'
    '\nВвод: ').split(',')]
    return contakt

def find_info():
    poisk = input('Введите фамилию для поиска (для выхода в предыдущее меню введите "q" без ковычек): ')
    return poisk