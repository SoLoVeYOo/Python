# Управляющие кострукции for

# for i in enumeration:
# # operator 1
# # operator 2
# # . . .
# # operator n

for i in 1,2,3,4,10,5:
    print(i**2)

list = [1,2,3,4,10,5]
for i in list:
    print(i**2)

r = range(10) # перечисление чисел от 0 до 10
for i in r:
    print(i)

for i in range(1, 4, 2): # от до (не включительно) с прыжком в 2
    print(i)

for i in 'qwe - rty':
    print(i)

r = range(100, 0, -20) # range(100, 0, -20)
for i in r:
    print(i)
# 100 80 60 40 20
for i in range(5):
    print(i)
# 0 1 2 3 4

line = ""
for i in range(5):
    line = ""
    for j in range(5):
        line += "*"
    print(line)