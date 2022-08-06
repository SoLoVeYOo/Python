# Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.

chisla = input('Введите числа через пробел: ')
with open(r'Homework\hw_test_lesson_6\findmaxmin.txt','w') as f:
        f.write(chisla)
with open(r'Homework\hw_test_lesson_6\findmaxmin.txt', 'r') as f:
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

find_max_min = lambda x, f: f(x)

print(f' Максимальное и минимальное числа в списке {spisok}: {find_max_min(spisok, max)} и {find_max_min(spisok, min)}')