# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

import random
from __init__ import *

with open(r'Seminar\prog_lesson_5\summa_mnogochlenov.txt','w') as my_file:
            my_file.write(f'{create_uravnenie()}')
            my_file.write(f'\n{create_uravnenie()}')           

with open(r'Seminar\prog_lesson_5\summa_mnogochlenov.txt', 'r') as my_file:
        lines = my_file.readlines()
        mnogochlen1, mnogochlen2 = lines[0], lines[1]

def find_koeficient (stroka: str) -> dict:
    koeficienty = {'a': 0, 'b': 0,'d': 0,'c': 0}
    stroka = stroka.replace(' + ', ' ')[:-4].split()
    for i in range(len(stroka)):
        if 'x^3' in stroka[i]: koeficienty['a'], stroka[i] = int(stroka[i].replace('x^3', '')), '0'
        if 'x^2' in stroka[i]: koeficienty['b'], stroka[i] = int(stroka[i].replace('x^2', '')), '0'
        if 'x' in stroka[i]: koeficienty['d'], stroka[i] = int(stroka[i].replace('x', '')), '0'
    if int(stroka[len(stroka)-1]) != 0: koeficienty['c'] = int(stroka[len(stroka)-1])
    return koeficienty

def summa_mnogochlenov (slovar1: dict, slovar2: dict) -> str:
    stroka = []
    a = slovar1['a'] + slovar2['a']
    b = slovar1['b'] + slovar2['b']
    d = slovar1['d'] + slovar2['d']
    c = slovar1['c'] + slovar2['c']
    if c != 0: stroka.append(f'{c}')
    if d != 0: stroka.append(f'{d}x')
    if b != 0: stroka.append(f'{b}x^2')
    if a != 0: stroka.append(f'{a}x^3')
    return ' + '.join(stroka[::-1]) + ' = 0'

koeficienty1 = find_koeficient(mnogochlen1)
koeficienty2 = find_koeficient(mnogochlen2)

with open(r'Seminar\prog_lesson_5\summa_mnogochlenov.txt','a') as my_file:
            my_file.write(f'\n{summa_mnogochlenov(koeficienty1, koeficienty2)}')

print(koeficienty1) # для проверки в терминале
print(koeficienty2) # для проверки в терминале
print(summa_mnogochlenov(koeficienty1, koeficienty2)) # для проверки в терминале