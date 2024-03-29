# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

import math

spisok_chisel = []
for i in input('Введите целые числа через пробел: ').split():
    try:
        i = int(i)
        spisok_chisel.append(i)
    except: 
        print('Ошибка! Введите целые числа!')
        exit()

def proizvedenie_chisel (spisok: list) -> list:
    spisok_out = []
    for i in range(math.ceil(len(spisok)/2)):
        spisok_out.append(spisok[i] * spisok[len(spisok)-1-i])
    return spisok_out

def proizvedenie_chisel_2 (spisok: list) -> list:
    spisok_out = []
    j, temp = 0, len(spisok) - 1
    while j <= temp:
        spisok_out.append(spisok[j] * spisok[temp])
        j += 1
        temp -= 1
    return spisok_out

print(f'Произведения парных чисел в списке {spisok_chisel} равны: {proizvedenie_chisel(spisok_chisel)}')
print(f'Произведения парных чисел в списке {spisok_chisel} равны: {proizvedenie_chisel_2(spisok_chisel)}')