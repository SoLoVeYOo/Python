import csv


def read_all_book():
    with open('PhoneBook.csv', newline='', encoding='UTF-8') as f:
            csv_f = csv.reader(f, delimiter=';')
            data = []
            for row in csv_f:
                data.append(row)
    return data


def read_exaclty(what_to_find):
    with open('PhoneBook.csv', newline='', encoding='UTF-8') as f:
            csv_f = csv.reader(f, delimiter=';')
            data_exactly = []
            for row in csv_f:
                for i in row:
                    if i==what_to_find:
                        data_exactly.append(row)
    return data_exactly