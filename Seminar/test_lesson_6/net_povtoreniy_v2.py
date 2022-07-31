# Дана последовательность чисел.
# Получить список уникальных элементов заданной последовательности.

chisla_in = input('Введите числа через пробел: ')
with open(r'Seminar\test_lesson_6\net_povtoreniy_v2.txt','w', encoding='utf-8') as my_file:
        my_file.write(chisla_in)
with open(r'Seminar\test_lesson_6\net_povtoreniy_v2.txt', 'r', encoding='utf-8') as my_file:
        chisla_out = my_file.read()

def perevod_stroki_v_spisok (stroka: str) -> list:
    spisok = list(map(int, stroka.split()))
    return spisok

def sort_net_povtoreniy (spisok: list) -> list:
    spisok_out = list(filter(lambda x: spisok.count(x) == 1, spisok))
    return spisok_out

def sort_net_povtoreniy_2 (stroka: str) -> list:
    '''
    все в одном (и перевод строки в список и сортировка)
    '''
    spisok_out = list(filter(lambda x: list(map(int, stroka.split())).count(x) == 1, list(map(int, stroka.split()))))
    return spisok_out

print(f'Список неповторяющихся элементов из списка {chisla_out} -> {sort_net_povtoreniy(perevod_stroki_v_spisok(chisla_out))}')

try:
    with open(r'Seminar\test_lesson_6\net_povtoreniy_v2.txt', 'a', encoding='utf-8') as my_file:
        my_file.write(f"\n{' '.join(map(str, sort_net_povtoreniy_2(chisla_out)))}")
    print(f'Список неповторяющихся элементов из списка {chisla_out} -> {sort_net_povtoreniy_2(chisla_out)}')
except: print('Ошибка! Введите целые числа!')