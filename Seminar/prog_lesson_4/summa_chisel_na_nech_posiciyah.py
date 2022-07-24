# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

spisok_chisel = []
for i in input('Введите целые числа через проблем: ').split():
    try:
        i = int(i)
        spisok_chisel.append(i)
    except:
        print('Ошибка! Введите целые числа!')
        exit()

def summa_chisel (spisok: list) -> int:
    summa = 0
    for j in range(1, len(spisok), 2): summa += spisok[j]
    return summa

print(f'Сумма чисел в списке {spisok_chisel} на нечетных позициях равна: {summa_chisel(spisok_chisel)}')