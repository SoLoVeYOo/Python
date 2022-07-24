# Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.

chisla = input('Введите числа через пробел: ')
with open(r'Seminar\test_lesson_4\findmaxmin.txt','w') as f:
        f.write(chisla)
with open(r'Seminar\test_lesson_4\findmaxmin.txt', 'r') as f:
        mystr = f.read()
mystr = mystr.split()
spisok = []
for i in range(len(mystr)):
    try:
        mystr[i] = int(mystr[i])
        spisok.append(mystr[i])
    except:
        print('Ошибка! Введите целые числа!')
        exit()

# spisok = []
# for i in input('Введите числа через пробел: ').split():
#     try:
#         i = int(i)
#         spisok.append(i)
#     except:
#         print('Ошибка! Введите целые числа!')
#         exit()

def find_max_min (spisok_in: list) -> dict:
    result = {}
    # max, min = spisok_in[0], spisok_in[0]
    # for i in spisok_in:
    #     if i > max: max = i
    #     if i < min: min = i
    # maxim, minim = max(spisok_in), min(spisok_in)
    result['максимально число'] = max(spisok_in)
    result['минимальное число'] = min(spisok_in)
    return result

print(find_max_min(spisok))
print(f' Максимальное и минимальное числа в списке {spisok}: {max(spisok)} и {min(spisok)}')