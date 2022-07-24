# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и
# минимальным значением дробной части элементов.

spisok_chisel = []
for i in input('Введите вещественные числа через пробел: ').split():
    try:
        proverka = float(i)
        spisok_chisel.append(i)
    except: 
        print('Ошибка! Введите вещественные числа!')
        exit()

def raznica_chastey (spisok_in: list) -> float:
    temp_list = []
    for i in spisok_in:
        i = float(i)
        if i - int(i) != 0:
            temp_list.append(i - int(i))
    raznost = round(max(temp_list) - min(temp_list), 3)
    return raznost

print(f'Разница между максимальным и минимальным значениям дробной части элементов списка {spisok_chisel} равна: {raznica_chastey(spisok_chisel)}')