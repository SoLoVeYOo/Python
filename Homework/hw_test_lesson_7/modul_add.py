import csv

def add_data(first_name, last_name, phone_number):
    with open(r'Homework\hw_test_lesson_7\data_base.csv', 'a', encoding='utf-8') as file:
            a = csv.writer(file, delimiter = ',', lineterminator='\r')
            a.writerow([f'{first_name}', f'{last_name}', f'{phone_number}'])