# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

spisok_chisel = []
for i in input('Введите целые числа через пробел: ').split():
    try:
        i = int(i)
        spisok_chisel.append(i)
    except: 
        print('Ошибка! Введите целые числа!')
        exit()

def proizvedenie_chisel (spisok: list) -> list: return [spisok[j] * spisok[len(spisok)-1-j] for j in range(int((len(spisok)+1)/2))]

print(f'Произведения парных чисел в списке {spisok_chisel} равны: {proizvedenie_chisel(spisok_chisel)}')