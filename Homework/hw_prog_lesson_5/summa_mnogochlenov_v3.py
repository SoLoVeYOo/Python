# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

import random

def slucgaynyy_mnogochlen () -> str: # алгоритм из предыдущей задачи для создания многочленов
    stroka = ''
    d = random.randint(0, 5)
    if d == 0: stroka += ''
    elif d == 1: stroka += f'x^3'
    else: stroka += f'{d}x^3'
    a = random.randint(0, 5)
    if a == 0: stroka += ''
    elif a == 1: stroka += f' + x^2'
    else: stroka += f' + {a}x^2'
    b = random.randint(0, 5)
    if b == 0: stroka += ''
    elif b == 1: stroka += f' + x'
    else: stroka += f' + {b}x'
    c = random.randint(0, 5)
    if c == 0: stroka += ''
    else: stroka += f' + {c}'
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
    stroka = stroka[:-4].split()
    koeficienty['a'] = int(stroka[0].replace('x^2', ''))
    if len(stroka) > 1:
        if 'x' in stroka[2]:
            koeficienty['b'] = int((stroka[1]+stroka[2]).replace('x', ''))
            if len(stroka) > 3: koeficienty['c'] = int(stroka[3]+stroka[4])
            else: koeficienty['c'] = 0
        else: koeficienty['b'], koeficienty['c'] = 0, int(stroka[1]+stroka[2])
    else: koeficienty['b'], koeficienty['c'] = 0, 0
    return koeficienty

def summa_mnogochlenov (slovar1: dict, slovar2: dict) -> str:
    stroka = ''
    stroka += f"{(slovar1['a'] + slovar2['a'])}x^2"
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