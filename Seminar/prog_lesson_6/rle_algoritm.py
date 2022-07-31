# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

import json

with open(r'Seminar\prog_lesson_6\rle_text.txt','r', encoding='utf-8') as my_file:
        my_text = my_file.read()

print(my_text) # для проверки в терминале

def rle_zip (stroka: str) -> list:
    rle_spisok, count = [], 1
    for i in range(1, len(stroka)):
        if stroka[i] == stroka[i-1]:
            count +=1
            if i == len(stroka)-1: rle_spisok.append((stroka[i], count))
        else:
            rle_spisok.append((stroka[i-1], count))
            count = 1
            if i == len(stroka)-1: rle_spisok.append((stroka[i], count))
    return rle_spisok

with open(r'Seminar\prog_lesson_6\rle_text.json','w', encoding='utf-8') as my_zip_file:
        my_zip_file.write(json.dumps(rle_zip(my_text), ensure_ascii=False))

with open(r'Seminar\prog_lesson_6\rle_text.json','r', encoding='utf-8') as my_zip_file:
        spisok = json.load(my_zip_file)

def rle_un_zip (spisok_in: list) -> str:
    result = ''.join([str(spisok_in[i][1]*spisok_in[i][0]) for i in range(len(spisok_in))])
    return result

print(rle_un_zip(spisok)) # для проверки в терминале

with open(r'Seminar\prog_lesson_6\rle_text.txt','a', encoding='utf-8') as my_file:
        my_file.write(f'\n{rle_un_zip(spisok)}')
