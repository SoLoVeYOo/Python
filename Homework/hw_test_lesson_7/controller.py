from modul_add import add_data as ad
from modul_find import find_number as fn
import view

def programm_work(name):   
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

def buttom_click():
    nickname = view.name_person()
    if nickname == 'q': exit()
    elif nickname == 'SoLoVeYOo':
        print('Добрый день, SoLoVeYOo!')
        while True:
            me = input('Введите'
            '\n"work" если хотите поработать'
            '\n"log" если хотите просмотреть логи'
            '\nили "q" для выхода из программы: ')
            if me == 'q': break
            elif me == 'log':
                with open(r'Homework\hw_prog_lesson_7\log.txt','r', encoding='utf-8') as file:
                    my_log = file.read()
                break
            elif me == 'work':
                programm_work(nickname)
                break
            else: print('Введите, пожалуйста, корректную команду.')
    else: programm_work(nickname)