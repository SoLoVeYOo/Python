# Функция map() применяет указанную функцию к
# каждому элементу итерируемого объекта и
# возвращает итератор с новыми объектами.
# f(x) ⇒ x + 10
# map(f, [ 1, 2, 3, 4, 5])
# ↓ ↓ ↓ ↓ ↓
# [ 11, 12, 13, 14, 15]
# Нельзя пройтись дважды


li = [x for x in range(1,20)]
li = list(map(lambda x: x+10, li))
print(li)

# data = list(map(int, input().split()))
# print(data)

# data = map(int, '1 2 3 4 555 6'.split())
# for e in data:
#     print(e)

data = map(int, '1 2 3 4 555 6'.split())
for e in data:
    print(e)
print('--')
for e in data: # будет выполнятся только 1 раз! иначе нужно присваевать тип данных, например list
    print(e)

