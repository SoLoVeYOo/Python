# Напишите программу которая принимает на вход 5 чисел и находит большее из них

chisla = []

# range(5) -> [0, 1, 2, 3, 4]
# range(5, 11) -> от 5 (включительно) до 11 (НЕ включительно)
# range(10, 100, 2) -> перебор всех числе в заданном диопазоне с шагом 2
# for i in range(5):
#     x = int(input('--> '))
#     chisla.append(x)
# print(chisla)
# max = chisla[0]
# for i in chisla:
#     if i > max: max = i
# print(f'Максимально число: {max}')

max = 0
for i in range(5):
    x = int(input('--> '))
    if i == 0: max = x
    elif x > max: max = x
print(f'Максимально число: {max}')