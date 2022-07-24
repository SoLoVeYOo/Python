# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

import random

def slucgaynyy_mnogochlen (k: int) -> str: #возьмем алгоритм из предыдущей задачи для создания многочленов
    stroka = ''
    a = random.randint(1, 5) # чтобы уравнение обязательно содержало x^2
    if a == 0: stroka += ''
    elif a == 1: 
        if k == 1: stroka += f'x^2'
        else: stroka += f'{k}x^2'
    else: stroka += f'{a*k}x^2'
    b = random.randint(0, 5)
    if b == 0: stroka += ''
    elif b == 1: 
        if k == 1: stroka += f' + x'
        else: stroka += f' + {k}x'
    else: stroka += f' + {b*k}x'
    c = random.randint(0, 5)
    if c == 0: stroka += ''
    else: stroka += f' + {c*k}'
    stroka += ' = 0'
    return stroka

with open(r'Homework\hw_test_lesson_4\summa_mnogochlenov.txt','w') as my_file:
            my_file.write(slucgaynyy_mnogochlen(2))
            my_file.write(f'\n{slucgaynyy_mnogochlen(3)}')           

with open(r'Homework\hw_test_lesson_4\summa_mnogochlenov.txt', 'r') as my_file:
        lines = my_file.readlines()
        mnogochlen1 = lines[0]
        mnogochlen2 = lines[1]

def find_koeficient (stroka: str) -> dict:
    koeficienty = {}
    stroka = stroka[:-4]
    stroka = stroka.split()
    a = stroka[0]
    a = a.replace('x^2', '')
    a = int(a)
    koeficienty['a'] = a
    if len(stroka) > 1:
        if 'x' in stroka[2]:
            b = stroka[1]+stroka[2]
            b = b.replace('x', '')
            b = int(b)
            koeficienty['b'] = b
            if len(stroka) > 3:
                c = stroka[3]+stroka[4]
                c = int(c)
                koeficienty['c'] = c
            else: koeficienty['c'] = 0
        else:
            koeficienty['b'] = 0
            c = stroka[1]+stroka[2]
            c = int(c)
            koeficienty['c'] = c
    else:
        koeficienty['b'] = 0
        koeficienty['c'] = 0
    return koeficienty

def summa_mnogochlenov (slovar1: dict, slovar2: dict) -> str:
    stroka = ''
    a = slovar1['a'] + slovar2['a']
    stroka += f'{a}x^2'
    b = slovar1['b'] + slovar2['b']
    if b == 0: stroka += ''
    elif b == 1: stroka += f' + x'
    else: stroka += f' + {b}x'
    c = slovar1['c'] + slovar2['c']
    if c == 0: stroka += ''
    else: stroka += f' + {c}'
    stroka += ' = 0'
    return stroka

koeficienty1 = find_koeficient(mnogochlen1)
koeficienty2 = find_koeficient(mnogochlen2)

with open(r'Homework\hw_test_lesson_4\summa_mnogochlenov.txt','a') as my_file:
            my_file.write(f'\n{summa_mnogochlenov(koeficienty1, koeficienty2)}')

print(koeficienty1) # для проверки в терминале
print(koeficienty2) # для проверки в терминале
print(summa_mnogochlenov(koeficienty1, koeficienty2)) # для проверки в терминале