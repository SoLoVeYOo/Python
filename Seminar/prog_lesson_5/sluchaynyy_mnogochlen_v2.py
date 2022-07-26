# Задана натуральная степень k. Сформировать случайным образом
# список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.

import random

number = input('Введите коэффициент: ')

def sluchaynyy_mnogochlen (k: int) -> str:
    stroka = ''
    if k == 3:
        a = random.randint(1, 5)
        if a == 0: stroka += ''
        elif a == 1: stroka += f'1x^3'
        else: stroka += f'{a}x^3' 
    if k >= 2:
        if k == 2: b = random.randint(1, 5)
        else: b = random.randint(0, 5)
        if b == 0: stroka += ''
        elif b == 1: stroka += f' + 1x^2'
        else: stroka += f' + {b}x^2'
    if k >= 1:
        if k == 1: d = random.randint(1, 5)
        else: d = random.randint(0, 5)
        if d == 0: stroka += ''
        elif d == 1: stroka += f' + 1x'
        else: stroka += f' + {d}x'
    c = random.randint(0, 5)
    if c == 0: stroka += ''
    else: stroka += f' + {c}'
    stroka += ' = 0'
    if k != 3: stroka = stroka[3:]
    return stroka

try: 
    number = int(number)
    with open(r'Seminar\prog_lesson_5\sluchaynyy_mnogochlen.txt','w') as my_file:
            my_file.write(sluchaynyy_mnogochlen(number))
    with open(r'Seminar\prog_lesson_5\sluchaynyy_mnogochlen.txt', 'r') as my_file: # для проверки в терминале
        print(my_file.read())
except: print('Ошибка! Введите целое число!')