# В файле хранятся числа, нужно выбрать четные и
# составить список пар (число; квадрат числа).

spisok = []
with open (r'Examples\lesson_3\spisok_chisel.txt', 'r') as my_file:
    spisok = my_file.read()
spisok = spisok.split()

spisok_result = [(int(i), int(i)**2) for i in spisok if int(i)%2==0]
print(spisok_result)

#
def select (function, col):
    return [function(x) for x in col]

def where(function, col):
    return [x for x in col if function(x)]

res = select(int, spisok)
print(res)
res = where(lambda x: not x%2, res)
print(res)
res = select(lambda x: (x, x**2), res)
print(res)

#
res = map(int, spisok)
res = where(lambda x: not x%2, res)
res = list(map(lambda x: (x, x**2), res))
print(res)

#
res = map(int, spisok)
res = filter(lambda x: not x%2, res)
res = list(map(lambda x: (x, x**2), res))
print(res)