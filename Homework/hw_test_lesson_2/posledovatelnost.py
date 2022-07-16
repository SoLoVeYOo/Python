# Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму

vvodnoe = input('Введите число: ')

def posledovatelnost (number: str) -> list:
    summa = 0
    result = []
    for i in range(1, int(number) + 1):
        element = round((1 + 1/i)**i, 3)
        result.append(element)
        summa += element
    print (result)
    print (f'Сумма чисел в списке равна: {summa}')

try:
    vvodnoe = int(vvodnoe)
    print(posledovatelnost(vvodnoe))
except: print('Введите целое число')