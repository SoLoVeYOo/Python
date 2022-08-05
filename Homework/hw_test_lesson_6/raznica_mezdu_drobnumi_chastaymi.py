# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и
# минимальным значением дробной части элементов.

spisok_chisel = []
for i in input('Введите вещественные числа через пробел: ').split():
    try:
        i = float(i)
        spisok_chisel.append(i)
    except: 
        print('Ошибка! Введите вещественные числа!')
        exit()

def raznica_chastey (spisok_in: list) -> float:
    temp_list = []
    for i in spisok_in:
        if float('0.' + str(i).split('.')[1]) != 0: # исключаем числа без дробных частей (целые числа)
            temp_list.append(float('0.' + str(i).split('.')[1]))
    max, min = temp_list[0], temp_list[0]
    for j in temp_list:
        if j > max: max = j
        if j < min: min = j
    raznost = max - min
    return raznost

print(f'Разница между максимальным и минимальным значениям дробной части элементов списка {spisok_chisel} равна: {raznica_chastey(spisok_chisel)}')