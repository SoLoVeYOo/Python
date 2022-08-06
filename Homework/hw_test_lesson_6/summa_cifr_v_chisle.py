# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

vvodnoe = input('Введите число: ')

def summa_v_chisle(chislo: str) -> int:
    summa = 0
    temp = chislo.split(".")
    temp1 = temp[0]
    temp2 = temp[1] 
    for i in range(len(temp1)): 
            summa += int(temp1[i])
    for i in range(len(temp2)): 
            summa += int(temp2[i])        
    return summa

try:
    proverka = float(vvodnoe)
    print(f'Сумма цифр в числе {vvodnoe} равна: {summa_v_chisle(vvodnoe)}')
except: print('Введите вещесвенное число без ошибки')