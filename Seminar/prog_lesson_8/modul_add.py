import csv

def add_contakt(first_name, last_name, phone_number):
    with open(r'Seminar\prog_lesson_8\data_base.csv', 'a', encoding='utf-8') as file:
            a = csv.writer(file, delimiter = ',', lineterminator='\r')
            a.writerow([f'{first_name}', f'{last_name}', f'{phone_number}'])
    print('Контакт успешно добавлен в записную книгу!')