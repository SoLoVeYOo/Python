# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

number = input('Введите число: ')

def summa_v_chisle(chislo: str) -> int:
    summa = 0
    chislo = chislo.replace('.', '') 
    for i in range(len(chislo)): 
        summa += int(chislo[i])   
    return summa

try:
    proverka = float(number)
    print(f'Сумма цифр в числе {number} равна: {summa_v_chisle(number)}')
except: print('Введите вещесвенное число без ошибки')


