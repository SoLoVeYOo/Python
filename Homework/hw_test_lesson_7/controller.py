from os import name
from modul_add import add_contakt as ac
from modul_find import find_number as fn
import view

def buttom_click():
    while True:
        vvod = input('Что вы желаете сделать? ('
        '\nВведите "1" если нужно добавить запись в телефонную книгу.'
        '\nВведите "2" если нужно найти запись в телефонной книге.'
        '\nВведите "q" для выхода из программы.'
        '\nВвод: ')
        if vvod == 'q': break
        elif vvod == '1':
            while True:
                temp1 = view.new_contakt()
                if temp1[0] == 'q': break
                if len(temp1) == 3: ac(temp1[0], temp1[1], temp1[2])
                else: print('Некорректный ввод данных!')
                print('Добавить еще один контакт?')
        elif vvod == '2':
            while True:
                temp2 = view.find_phone()
                if temp2 == 'q': break
                else: view.return_find_result(temp2, fn(temp2))
                print('Продолжить поиск?')
        else: print('Вы ввели некорректные данные, попробуйте еще раз.')