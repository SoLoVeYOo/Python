# Дан список чисел. Создайте список, в который попадают числа,
# описываемые возрастающую последовательность. Порядок элементов менять нельзя.

my_list = [2, 1, 5, 1, 4, 2, 3, 6, 7, 9, 9, 8]

spisok_out = []

def istina (spisok):
    for k in range(1, len(spisok)):
        if spisok[k] == spisok[k-1]+1: x = True
        else:
            x = False
            break
    return x

def selection_sort(spisok: list) -> list:
    for j in range(len(spisok)):
        min_position = j
        for k in range(len(spisok)):
            if (spisok[k] > spisok[min_position]): min_position = k
            spisok[min_position], spisok[j] = spisok[j], spisok[min_position]

for i in range(len(my_list)):
    for j in range(len(my_list)-1, i, -1):
        temp = list(my_list[i+1: j])
        if len(temp) < 4: break
        selection_sort(temp)
        if istina(temp) == True:
            spisok_out = [my_list[i], my_list[j]]
            break
    if istina(temp) == True: break
    
print(spisok_out)