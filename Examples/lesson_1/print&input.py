# типы данных и переменные
# int  # целые
# float  # вещественные
# boolean  # логические
# str  # строки
# list  # хранилища (массивы)

# Вывод данных

value = None
print(type(value))
a = 123
b = 1.23
print(type(a))
print(type(b))
value = 1234
print(type(value))
s = 'hello "world"'  # можно ' или " для того чтобы то или иное показать в строке
print(s)
print(a, ' - ', b, ' - ', s)
print('{} - {} - {}'.format(a, b, s))
print('{1} - {2} - {0}'.format(a, b, s))
print(f'{a} - {b} - {s}')
f = True
t = False
print(f, t)

list = [1, 2, 3]
con = [1, 2, 3, 'hello', 1.23]
print(list)
print(con)


# Ввод и вывод данных
print('Введите a =')
# необходимо указать какой именно тип данных нужен, по умолчанию используется строка
a = int(input())
print('Введите b = ')
b = float(input())
print(a, ' + ', b, ' = ', a+b)

a = int(input('Введите а: ')) # 11
b = int(input('Введите b: ')) # 22
c = 33
print('{} + {} = {}'.format(a, b, c)) # 11 + 22 = 33

a = int(input('Введите \nа: '))
b = int(input('Введите \nb: '))
c = a + b
print('{} + {} = {}'.format(a, b, c))