def name_user():
    username = input('Введите имя пользователя (для выхода в предыдущее меню введите "q" без ковычек): ')
    return username

def new_info():
    information = [i for i in input('Введите данные "фамилия" "имя" "телефон" "класс" "пол" через запятую (без ковычек),'
    '\nкоторые хотите добавить (если данных нет, то введите "-"'
    '\n(для выхода в предыдущее меню введите "q" без ковычек).'
    '\nВвод: ').split(',')]
    return information

def find_info():
    poisk = [i for i in input('Введите критерий поиска:'
    '\nесли "фамилия" введите 1,'
    '\n"имя" - 2, "телефон" - 3, "класс" - 4, "пол" - 5 через запятую (без ковычек),'
    '\nкоторые хотите добавить (если данных нет, то введите "-"'
    '\n(для выхода в предыдущее меню введите "q" без ковычек).'
    '\nВвод: ').split(',')]
    return poisk

def return_find_result(zapros, resultat): # отредактировано
    print(f'{zapros}, вывод результата по заданному запросу: {resultat}')