# Дан список чисел. Создайте список, в который попадают числа,
# описываемые возрастающую последовательность. Порядок элементов менять нельзя.

my_list = [1, 5, 2, 3, 4, 1, 7]

def find_posled (spisok_in):
    spisok_out = []
    temp = []
    for i in range(1, len(spisok_in)-2):
        for j in range(1, len(spisok_in)-2):
            if spisok_in[j] - 1 == spisok_in[i]:


        if spisok_in[i] > spisok_in[i-1]:
            if i == len(spisok_in)-1:
                temp.append(spisok_in[i])
                spisok_out.append(temp)
            else: temp.append(spisok_in[i])
        else:
            if len(temp) > 1:
                spisok_out.append(temp)
                temp = []
                temp.append(spisok_in[i])
            else:
                temp = []
                temp.append(spisok_in[i])
    return spisok_out

print(find_posled(my_list))