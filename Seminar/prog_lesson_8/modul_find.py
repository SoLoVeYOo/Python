import csv

def find_number(last_name):
    with open(r'Seminar\prog_lesson_8\data_base.csv', encoding='utf-8') as file:
        filereader = csv.reader(file, delimiter=",")
        temp = False
        for row in filereader:
            if row[0] == last_name:
                temp, tel = True, row[2]
        if temp == True:
            return tel
        else: return 'номер отсутствует, либо данной записи в телефонной книге нет'