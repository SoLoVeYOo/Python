# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

import random
from __init_ import sluchaynyy_mnogochlen

with open(r'Seminar\prog_lesson_5\summa_mnogochlenov.txt','w') as my_file:
            my_file.write(sluchaynyy_mnogochlen(random.randint(1,4)))
            my_file.write(f'\n{sluchaynyy_mnogochlen(random.randint(1,4))}')           

with open(r'Seminar\prog_lesson_5\summa_mnogochlenov.txt', 'r') as my_file:
        lines = my_file.readlines()
        mnogochlen1, mnogochlen2 = lines[0], lines[1]

def find_koeficient (stroka: str) -> dict:
    koeficienty = {'a': 0, 'b': 0,'d': 0,'c': 0}
    stroka = stroka[:-4].split()
    for i in range(len(stroka)):
        if 'x^3' in stroka[i]: koeficienty['a'], stroka[i] = int(stroka[i].replace('x^3', '')), '0'
        if 'x^2' in stroka[i]:
            if stroka[0] != 0: koeficienty['b'], stroka[i] = int(stroka[i].replace('x^2', '')), '0'
            else: koeficienty['b'], stroka[i] = int((stroka[i-1]+stroka[i]).replace('x^2', '')), '0'
        if 'x' in stroka[i]:
            if stroka[0] != 0: koeficienty['d'], stroka[i] = int(stroka[i].replace('x', '')), '0'
            else: koeficienty['d'], stroka[i] = int((stroka[i-1]+stroka[i]).replace('x', '')), '0'
    if int(stroka[len(stroka)-1]) != 0: koeficienty['c'] = int(stroka[len(stroka)-1])
    return koeficienty

def summa_mnogochlenov (slovar1: dict, slovar2: dict) -> str:
    stroka = ''
    a = slovar1['a'] + slovar2['a']
    if a == 0: stroka += ''
    elif a == 1: stroka += f'x^3'
    else: stroka += f'{a}x^3'
    b = slovar1['b'] + slovar2['b']
    if b == 0: stroka += ''
    elif b == 1: stroka += f' + 1x^2'
    else: stroka += f' + {b}x^2'
    d = slovar1['d'] + slovar2['d']
    if d == 0: stroka += ''
    elif d == 1: stroka += f' + 1x'
    else: stroka += f' + {d}x'
    c = slovar1['c'] + slovar2['c']
    if c == 0: stroka += ''
    else: stroka += f' + {c}'
    stroka += ' = 0'
    if a == 0: stroka = stroka[3:]
    return stroka

koeficienty1 = find_koeficient(mnogochlen1)
koeficienty2 = find_koeficient(mnogochlen2)

with open(r'Seminar\prog_lesson_5\summa_mnogochlenov.txt','a') as my_file:
            my_file.write(f'\n{summa_mnogochlenov(koeficienty1, koeficienty2)}')

print(koeficienty1) # для проверки в терминале
print(koeficienty2) # для проверки в терминале
print(summa_mnogochlenov(koeficienty1, koeficienty2)) # для проверки в терминале