import csv

def find_number(last_name):
    with open(r'Homework\hw_test_lesson_7\data_base.csv', encoding='utf-8') as file:
        filereader = csv.reader(file, delimiter=",")

    temp = False
    for r in filereader:
        if r[0] == last_name:
            temp, tel = True, r[2]
    if temp == True:
        return tel
    else: return 'Данной фамилли в записной книжке нет'