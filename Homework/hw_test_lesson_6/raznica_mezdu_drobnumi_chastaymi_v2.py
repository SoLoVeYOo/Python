# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и
# минимальным значением дробной части элементов.

spisok = []
for i in input('Введите вещественные числа через пробел: ').split():
    try:
        i = float(i)
        spisok.append(i)
    except: 
        print('Ошибка! Введите вещественные числа!')
        exit()

def sort_spisok (spisok_in: list) -> float:
    return [float('0.' + str(i).split('.')[1]) for i in spisok_in if float('0.' + str(i).split('.')[1]) != 0]

raz = lambda x,y: x - y

print(f'Разница между максимальным и минимальным значениям дробной части элементов списка {spisok}'
    f' равна: {raz(max(sort_spisok(spisok)), min(sort_spisok(spisok)))}')