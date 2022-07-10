# Управляющая конструкция while, while-else
# while condition:
# # operator 1
# # operator 2
# # . . .
# # operator n

# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# print(inverted)

# while condition:
# # operator 1
# # operator 2
# # . . .
# # operator n
# else:
# # operator n + 1
# # operator n + 2
# # . . .
# # operator n + m

original = 23
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
else:
    print('Пожалуй')
    print('хватит )')
print(inverted)