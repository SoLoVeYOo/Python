# В файле хранятся числа, нужно выбрать четные и
# составить список пар (число; квадрат числа).

spisok = []
with open (r'Examples\lesson_3\spisok_chisel.txt', 'r') as my_file:
    spisok = my_file.read()
spisok = spisok.split()

spisok_result = [(int(i), int(i)**2) for i in spisok if int(i)%2==0]
print(spisok_result)