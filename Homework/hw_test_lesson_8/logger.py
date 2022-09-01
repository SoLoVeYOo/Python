from datetime import datetime as dt
from time import time

def log(imya_polzovatelya, stroka_primer, stroka_result): # отредактированно
    time = dt.now().strftime('%H:%M')
    with open(r'Homework\hw_test_lesson_8\log.txt', 'a', encoding='utf-8') as file:
        file.write('пользователь: {} | время: {} | запрос: {} | результат: {}\n'
                    .format(imya_polzovatelya, time, stroka_primer, stroka_result))