# Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.

spisok = []
for i in input('Введите числа через пробел: ').split():
    try:
        i = int(i)
        spisok.append(i)
    except:
        print('Ошибка! Введите целые числа!')
        exit()

def find_max_min (spisok_in: list) -> dict:
    result = {}
    max, min = spisok_in[0], spisok_in[0]
    for i in spisok_in:
        if i > max: max = i
        if i < min: min = i
    result['максимально число'] = max
    result['минимальное число'] = min
    return result

print(find_max_min(spisok))