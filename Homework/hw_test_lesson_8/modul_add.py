import csv

def add_contakt(first_name, last_name, phone_number, klass, pol):
    try:
        with open(r'Homework\hw_test_lesson_8\data_base.csv', 'a', encoding='utf-8') as file:
                a = csv.writer(file, delimiter = ',', lineterminator='\r')
                a.writerow([f'{first_name}', f'{last_name}', f'{phone_number}', f'{klass}', f'{pol}'])
        return True
    except: return False