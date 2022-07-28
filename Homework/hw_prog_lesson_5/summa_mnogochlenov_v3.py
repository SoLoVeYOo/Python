# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

import random
from __init_ import *

with open(r'Homework\hw_prog_lesson_5\summa_mnogochlenov.txt','w') as my_file:
            my_file.write(f'{create_uravnenie()}')
            my_file.write(f'\n{create_uravnenie()}')           

with open(r'Homework\hw_prog_lesson_5\summa_mnogochlenov.txt', 'r') as my_file:
        lines = my_file.readlines()
        mnogochlen1, mnogochlen2 = lines[0], lines[1]

def find_koeficient (stroka: str) -> dict:
    koeficienty = {}
    stroka = stroka.replace(' + ', ' ')[:-4].split()
    for i in range(len(stroka)):
        if 'x^' in stroka[i]:
            koeficienty[int(stroka[i].split('x^')[1])] = int(stroka[i].split('x^')[0])
        elif 'x' in stroka[i]: 
            koeficienty[1] = int(stroka[i].split('x')[0])
        else: koeficienty[0] = int(stroka[i])
    return koeficienty

def summa_mnogochlenov (slovar1: dict, slovar2: dict) -> str:
    stroka = []
    for s1, k1 in slovar1.items():
        temp = False
        for s2, k2 in slovar2.items():
            if s1 == s2:
                if s1 > 1 and k1+k2 != 0: stroka.append(f'{k1+k2}x^{s1}')  
                elif s1 == 1 and k1+k2 != 0:stroka.append(f'{k1+k2}x')
                elif k1+k2 != 0: stroka.append(f'{k1+k2}')
                temp = True
                continue
        if temp == False: 
            if s1 > 1: stroka.append(f'{k1}x^{s1}')
            elif s1 == 1: stroka.append(f'{k1}x')
            else: stroka.append(f'{k1}')
    for s2, k2 in slovar2.items():
        temp = False
        for s1, k1 in slovar1.items():
            if s2 == s1:
                temp = True
                continue
        if temp == False:
            if s2 > 1: stroka.append(f'{k2}x^{s2}')
            elif s2 == 1: stroka.append(f'{k2}x')
            else: stroka.append(f'{k2}')
    stroka.reverse()     
    return ' + '.join(stroka[::-1]) + ' = 0'

koeficienty1 = find_koeficient(mnogochlen1)
koeficienty2 = find_koeficient(mnogochlen2)

with open(r'Homework\hw_prog_lesson_5\summa_mnogochlenov.txt','a') as my_file:
            my_file.write(f'\n{summa_mnogochlenov(koeficienty1, koeficienty2)}')

print(summa_mnogochlenov(koeficienty1, koeficienty2)) # для проверки в терминале