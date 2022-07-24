# Задана натуральная степень k. Сформировать случайным образом
# список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.

import random

number = input('Введите коэффициент: ')

def slucgaynyy_mnogochlen (k: int) -> str:
    stroka = ''
    a = random.randint(1, 99) # чтобы уравнение обязательно содержало x^2
    if a == 1: 
        if k == 1: stroka += f'x^2'
        else: stroka += f'{k}x^2'
    else: stroka += f'{a*k}x^2'
    b = random.randint(0, 99)
    if b == 0: stroka += ''
    elif b == 1: 
        if k == 1: stroka += f' + x'
        else: stroka += f' + {k}x'
    else: stroka += f' + {b*k}x'
    c = random.randint(0, 99)
    if c == 0: stroka += ''
    else: stroka += f' + {c*k}'
    stroka += ' = 0'
    return stroka

try: 
    number = int(number)
    with open(r'Homework\hw_test_lesson_4\sluchaynyy_mnogochlen.txt','w') as my_file:
            my_file.write(slucgaynyy_mnogochlen(number))
    with open(r'Homework\hw_test_lesson_4\sluchaynyy_mnogochlen.txt', 'r') as my_file: # для проверки в терминале
        print(my_file.read())
except: print('Ошибка! Введите целое число!')