import save_con as save_con
import read_con as read_con
import export as e_xml

def do_it():
    question = input(f'Выберите действие и нажмите: 1- добавить контакт, 2- найти контакт, 3-посмотреть всю книгу, 4 - импортировать тел.книгу ')
    if question=="1":
        save_con.write_to_file()
    elif question=="2":
        for i in read_con.read_exaclty(input('Enter seach:')):
            print(i)
    elif question=="3":
        for i in read_con.read_all_book():
            print(i)
    elif question=="4":
        e_xml.export_to_xml()  
    else:
        print('Введено не корректное число')
        return do_it()