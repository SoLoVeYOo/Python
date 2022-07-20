# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. сохраните список в формате JSON.
import json
from unittest import result

vvodnoe = input('Введите число ')

def sozdanie_spiska(chislo: int) -> list:
    # result = []
    # for i in range(chislo*2+1):
    #     result.append(-chislo+i)
    result = list(range(-chislo, chislo + 1))
    return result

try:
    vvodnoe = int(vvodnoe)
    zadannyi_spisok = sozdanie_spiska(vvodnoe)
    print(zadannyi_spisok)
except: print('Введите целое число')

with open('prog_lesson_3.json', 'w', encoding='utf-8') as fh:
    fh.write(json.dumps(zadannyi_spisok, ensure_ascii=False))
print('Данные формата Json успешго сохранены')

with open('prog_lesson_3.txt', 'w') as fh:
    fh.write(str(zadannyi_spisok))
print("Данные сохранены в txt")