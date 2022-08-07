from datetime import datetime as dt
from time import time

def log(imya_polzovatelya, stroka_primer, stroka_result):
    time = dt.now().strftime('%H:%M')
    with open('Seminar\prog_lesson_7\log.txt', 'a', encoding='utf-8') as file:
        file.write('пользователь: {} | время: {} | пример: {} | ответ: {}\n'
                    .format(imya_polzovatelya, time, stroka_primer, stroka_result))