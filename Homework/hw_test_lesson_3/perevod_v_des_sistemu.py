# Напишите программу, которая будет преобразовывать десятичное число в двоичное

chislo = input('Введите целое число для перевода: ')
system = input('Введите в какую систему необходимо перевести число: ')

def perevod_chisel (chislo_in: int, system_in: int) -> str:
    result = ''
    simvoly = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    while chislo_in > 0:
        ostatok = chislo_in // system_in
        result = simvoly[chislo_in - system_in * ostatok] + result
        chislo_in //= system_in
    return result

try:
    chislo = int(chislo)
    system = int(system)
    print(f'Число {chislo} в {system} системе --> {perevod_chisel(chislo, system)}')
except: print('Ошибка! Введите целые числа!')