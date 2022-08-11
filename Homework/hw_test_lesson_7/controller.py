from os import name
from modul_add import add_data as ad
from modul_find import find_number as fn
import view

def buttom_click():
    while True:
        vvod = input('Что бы вы хотели сделать?'
        '\nВведите "1" если хотите добавить запись в телефонную книгу.'
        '\nВведите "2" если хотите найти запись в телефонной книге.'
        '\nВведите "q" для выхода из программы.'
        '\nВвод: ')
        if vvod == 'q': break
        elif vvod == '1':
            while True:
                temp1 = view.add_new()
                if temp1[0] == 'q': break
                else: ad(temp1[0], temp1[1], temp1[2])
                print('Хотите добавить еще один контакт?')
        elif vvod == '2':
            while True:
                temp2 = view.print_find
                if temp2 == 'q': break
                else: print(fn(temp2))
                print('Хотите найти еще один контакт?')
        else: print('Вы ввели некорректные данные, попробуйте еще.')