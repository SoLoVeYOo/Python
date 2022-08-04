# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

vvodnoe = input('Введите число: ')

def summa_v_chisle(chislo: str) -> int:
    summa = 0
    chislo = chislo.replace('.', '') 
    for i in range(len(chislo)): 
        summa += int(chislo[i])   
    return summa

try:
    proverka = float(vvodnoe)
    print(f'Сумма цифр в числе {vvodnoe} равна: {summa_v_chisle(vvodnoe)}')
except: print('Введите вещесвенное число без ошибки')


