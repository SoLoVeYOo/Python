from modul_add import add_info as ai
from modul_find import find_number as fn
import view

def buttom_click():
    while True:
        nickname = view.name_user()
        if nickname == 'q': break
        elif nickname == 'SoLoVeYOo':
            print('Добрый день, SoLoVeYOo!')
            while True:
                comanda = input('Введите'
                '\n"work" если хотите поработать'
                '\n"log" если хотите просмотреть логи'
                '\nили "q" для выхода из программы: ')
                if comanda == 'q': break
                elif comanda == 'log':
                    with open(r'Homework\hw_test_lesson_8\log.txt','r', encoding='utf-8') as file:
                        my_log = file.read()
                    break
                elif comanda == 'work':
                    programm_work(nickname)
                    break
                else: print('Введите, пожалуйста, корректную команду.')
        else: programm_work(nickname)



def programm_work(nickname_user):
    while True:
        comanda = input('Что вы желаете сделать? ('
        '\nВведите "1" если нужно добавить запись в базу учеников.'
        '\nВведите "2" если нужно найти запись ученика.'
        '\nВведите "3" если нужно изменить запись ученика.'
        '\nВведите "q" для выхода из программы.'
        '\nВвод: ')
        if comanda == 'q': break
        elif comanda == '1':
            while True:
                temp1 = view.new_info()
                if temp1[0] == 'q': break
                if len(temp1) == 5: ai(temp1[0], temp1[1], temp1[2], temp1[3], temp1[4])
                else: print('Некорректный ввод данных!')
                print('Добавить еще одну запись?')
        elif comanda == '2':
            while True:
                temp2 = view.find_info()
                if temp2 == 'q': break
                else: view.return_find_result(temp2, fn(temp2))
                print('Продолжить поиск?')
        elif comanda == '3':
            while True:
                temp3 = 
        else: print('Вы ввели некорректные данные, попробуйте еще раз')


def programm_work2(name):   
    while True:
        primer = view.get_primer()
        if primer == 'q': break
        try:
            result = con(primer)
            if result == 'q':
                print('Выражение введено с ошибками. Запустите программу заного и введите, пожалуйста, выражение верно.')
                log(name, primer, 'выражение было введено с ошибками.')
                continue
            result = dec(result)
            log(name, primer, result)
            view.view_result(primer, result)
        except:
            print('Выражение введено с ошибками. Введите, пожалуйста, выражение верно.')
            log(name, primer, 'выражение было введено с ошибками.')
            continue