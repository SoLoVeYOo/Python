def view_result(primer, result):
    print(f'{primer} = {result}')

def add_new():
    return input('Введите данные "фамилия" "имя" "телефон" которые хотите добавить через запятую: ').split(',')

def print_find():
    return input('Введите имя пользователя (для выхода, введите "q" без ковычек): ')