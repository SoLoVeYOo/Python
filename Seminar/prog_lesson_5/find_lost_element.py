# В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1].
# Найдите это число.

with open (r'Seminar\prog_lesson_5\find_lost_element.txt', 'r') as my_file:
    spisok = my_file.readline()

spisok = [int(i) for i in spisok.split()]
spisok_out = []
[spisok_out.append(spisok[i]-1) for i in range(1, len(spisok)) if spisok[i] != spisok[i-1]+1]
if len(spisok_out) == 0: spisok_out = str('Таких чисел нет')
else: spisok_out = list(set(spisok + spisok_out))

with open (r'Seminar\prog_lesson_5\find_lost_element.txt', 'a', encoding='utf-8') as my_file:
    my_file.write(f'\n{spisok_out}')