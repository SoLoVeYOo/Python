# Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.

chisla_in = input('Введите числа через пробел: ')
with open(r'Homework\hw_test_lesson_4\net_povtoreniy.txt','w') as my_file:
        my_file.write(chisla_in)
with open(r'Homework\hw_test_lesson_4\net_povtoreniy.txt', 'r') as my_file:
        chisla_out = my_file.read()

chisla_out = chisla_out.split()

def net_povtoreniy (spisok_in: list) -> list:
    spisok_out = []
    for i in spisok_in:
        schetchik = 0
        for j in spisok_in:
            if j == i: schetchik += 1
        if schetchik == 1: spisok_out.append(i)
    return spisok_out

try:
    for i in chisla_out:
        i = int(i)
    print(f'Список неповторяющихся элементов из списка {chisla_out} -> {net_povtoreniy(chisla_out)}')
except: print('Ошибка! Введите целые числа!')