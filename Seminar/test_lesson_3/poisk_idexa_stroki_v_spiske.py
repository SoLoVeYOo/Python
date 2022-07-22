# Напишите программу, которая определит позицию второго 
# вхождения строки в списке либо сообщит, что её нет.

spisok = []
for j in input('Введите строки через пробел: ').split():
    spisok.append(j)
# spisok = ["123", "234", 123, "567"] # вводилась отдельно, так как не хватает знания синтаксиса, чтобы вводить с клавиатуры сразу и числа и строки   
stroka = input('Введите строку для поиска: ')

def poisk_sovpadeniy(a: list, b: str) ->int:
    schetchik = 0
    find_index = False
    for i in range(len(a)):
        if b == a[i]: schetchik +=1
        if schetchik == 2:
            find_index = i
            break
    return find_index

if poisk_sovpadeniy(spisok, stroka) == False:
    print(f'Позиции второго вхождения строки "{stroka}" в списке {spisok} нет')
else: print(f'Позиция второго вхождения строки "{stroka}" в списке {spisok}: {poisk_sovpadeniy(spisok, stroka)}')