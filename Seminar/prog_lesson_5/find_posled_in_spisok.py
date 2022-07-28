# Дан список чисел. Создайте список, в который попадают числа,
# описываемые возрастающую последовательность. Порядок элементов менять нельзя.

my_list = [1, 5, 2, 3, 4, 1, 6, 7, 9, 9, 1]

# def find_posled (spisok_in):
spisok_out = []
a = 0
b = len(my_list)-1

def istina (spisok):
    for i in range(1, len(spisok)):
        if spisok[i] != spisok[i-1]+1:
            return False
            break
    return True

for a in 
while b != a+1:
    count = 1
    temp = list(set(my_list[a+1: b]))
    if istina(temp) == True:
        spisok_out = [my_list[a], my_list[b]]
        break
    else:
        if count % 2 != 0: a += 1
        else: b -= 1
        count += 1

print(a, b)
print(spisok_out)

# for i in range(1, len(spisok_in)-2):
#     for j in range(1, len(spisok_in)-2):
#         if spisok_in[j] - 1 == spisok_in[i]:


    #     if spisok_in[i] > spisok_in[i-1]:
    #         if i == len(spisok_in)-1:
    #             temp.append(spisok_in[i])
    #             spisok_out.append(temp)
    #         else: temp.append(spisok_in[i])
    #     else:
    #         if len(temp) > 1:
    #             spisok_out.append(temp)
    #             temp = []
    #             temp.append(spisok_in[i])
    #         else:
    #             temp = []
    #             temp.append(spisok_in[i])
    # return spisok_out

# print(find_posled(my_list))