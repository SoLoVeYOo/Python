# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

from functools import reduce

vvodnoe = input('Введите число: ')

def summa_v_chisle(chislo: str) -> int:
    chislo = chislo.replace('.', '')
    summa = reduce(lambda x,y: x + y, [int(chislo[i]) for i in range(len(chislo))])  
    return summa

try:
    proverka = float(vvodnoe)
    print(f'Сумма цифр в числе {vvodnoe} равна: {summa_v_chisle(vvodnoe)}')
except: print('Введите вещесвенное число без ошибки')