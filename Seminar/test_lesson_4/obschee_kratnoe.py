# Задайте два числа. Напишите программу,
# которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

chislo_1 = input('Введите первое число: ')
chislo_2 = input('Введите второе число: ')


def poisk_nok (a:int, b: int) -> int:
    if b > a: a, b = b, a
    temp1, temp2 = a, b
    ostatok = 1
    while ostatok != 0:
        nod = temp2
        ostatok = temp1 % temp2
        temp1, temp2 = temp2, ostatok
    result = a * b / nod
    return int(result)

try:
    chislo_1 = int(chislo_1)
    chislo_2 = int(chislo_2)
    print(f'Наименьшим общим кратным чисел {chislo_1} и {chislo_2} является: {poisk_nok(chislo_1, chislo_2)}')
except: print('Ошибка! Введите целые числа!')