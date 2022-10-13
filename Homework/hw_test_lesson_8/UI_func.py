import csv
from unicodedata import name

def id():
    with open('PhoneBook.csv', newline='', encoding='UTF-8') as f:
        reader = csv.reader(f)
        data = list(reader)
        id = len(data) + 1
        return id
id()

def username():
    username = input('Please write your name here: ')
    return username

def surname():
    surname = input('Please write your surname here: ')
    return surname

def phone():
    phone_num = input('Please write your phone number here: ')
    return phone_num

def comments():
    comments = input('Please write any comments here (If there are no comments, leave the field blank): ')
    return comments