# Дан список чисел. Создайте список, в который попадают числа,
# описываемые возрастающую последовательность. Порядок элементов менять нельзя.

my_list = [5, 1, 2, 3, 6, 7]

spisok_out = []

def istina (spisok):
    for k in range(1, len(spisok)):
        if spisok[k] != spisok[k-1]+1:
            return False
            break
    return True

for i in range(len(my_list)):
    print(i)
    for j in range(len(my_list)-1, i, -1):
        if i+1 == j: break
        print(j)
        temp = list(set(my_list[i+1: j]))
        print(temp)
        if istina(temp) == True:
            spisok_out = [my_list[i], my_list[j]]
            break
        print(istina(temp)) 
    
print(spisok_out)