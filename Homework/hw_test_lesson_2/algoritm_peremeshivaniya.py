# Реализуйте алгоритм перемешивания списка.

from random import randint

numbers = []
for i in range(5):
    numbers.append(randint(-10, 10))

def selection_sort(spisok: list) -> list:
    for j in range(len(spisok)):
        min_position = j
        k = j + 1
        for k in range(len(spisok)):
            if (spisok[k] < spisok[min_position]):
                min_position = k
            temp = spisok[j]
            spisok[j] = spisok[min_position]
            spisok[min_position] = temp

print(numbers)
selection_sort(numbers)
print(numbers)