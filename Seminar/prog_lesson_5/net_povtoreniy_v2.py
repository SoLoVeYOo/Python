# Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.

chisla_in = input('Введите числа через пробел: ')
with open(r'Seminar\prog_lesson_5\net_povtoreniy.txt','w') as my_file:
        my_file.write(chisla_in)
with open(r'Seminar\prog_lesson_5\net_povtoreniy.txt', 'r') as my_file:
        chisla_out = my_file.read()

def net_povtoreniy (spisok_in: list) -> list:
    spisok_out = []
    for i in spisok_in:
        schetchik = 0
        for j in spisok_in:
            if j == i: schetchik += 1
        if schetchik == 1: spisok_out.append(i)
    return spisok_out

try:
    chisla_out = [int(i) for i in chisla_out.split()]
    print(f'Список неповторяющихся элементов из списка {chisla_out} -> {net_povtoreniy(chisla_out)}')
except: print('Ошибка! Введите целые числа!')

numbers =[1,2,3,4,4,1,0,8,5,6,7,8,0,8,4]
def UniqueNumbers(numbers):
    result=[]
    for i in numbers:
        if numbers.count(i)==1:
            result.append(i)
    return result
print(UniqueNumbers(numbers))