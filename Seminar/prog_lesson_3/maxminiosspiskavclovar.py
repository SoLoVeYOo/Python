# Напишите программу, которая на вход принимаеть список, а выводит словарь с показаниями:
# максимальное число
# минимальное число
# индекс максимального числа
# индекс минимального числа
# среднеарифметическое число

spisok = []
for j in input('Введите числа через пробел: ').split():
    try:
        j = int(j)
        spisok.append(j)
    except: print('Введите список из целых чисел')
    
def find_max_and_min(numbers: list) -> dict:
    max, min = numbers[0], numbers[0]
    index_max, index_min = 0, 0
    summa = 0
    for i in range(len(numbers)):
        if numbers[i] > max: max, index_max = numbers[i], i
        if numbers[i] < min: min, index_min = numbers[i], i
        summa += numbers[i]
    srednearifm = summa/len(numbers)
    result = {}
    result['максимальный элемент'] = max
    result['минимальный элемент'] = min
    result['индекс максимального элемента'] = index_max
    result['индекс минимального элемента'] = index_min
    result['среднеарифметическое'] = srednearifm
    return result

# try:
#     for i in spisok:
#         i = int(i)
#     print(find_max_and_min(spisok))
# except: print('Введите список из целых чисел')

print(find_max_and_min(spisok))
