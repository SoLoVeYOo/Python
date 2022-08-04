# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях.

vvodnoe = int(input('Введите число '))
iskomye = []
for j in input('Введите позиции через пробел ').split():
    iskomye.append(int(j))

def sozdanie_spiska(chislo: int) -> list:
    result = []
    for i in range(chislo*2+1):
        result.append(-chislo+i)
    return result

def proizvedenie(spisok: list, position: list) -> int:
    result = 1
    for i in position:
        result *= spisok[i]
    return result

try:
    vvodnoe = int(vvodnoe)
    zadannyi_spisok = sozdanie_spiska(vvodnoe)
    print(zadannyi_spisok)
    print(f'Произведение чисел на позициях {iskomye} равно: {proizvedenie(zadannyi_spisok, iskomye)}')
except: print('Введите целое число')
