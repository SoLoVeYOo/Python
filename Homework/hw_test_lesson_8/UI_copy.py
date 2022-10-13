def get_user_data(users):
    phonebook={}
    print ('Введите информацию о контакте в последовательности Имя, Фамилия, Тел номер, примечание')
    name = input('Enter user name: ')
    surname = input('Enter user surname: ')
    phone_number = input('Enter user phone number: ')
    comment = input('Enter comments: ')
    you_sure = input(f'Хотите скорректировать (yes/no): ').lower()
    if you_sure == 'yes':
        return get_user_data()
    elif you_sure == 'no':
        phonebook.update({'Name': name, 'Surname': surname, 'Phone number': phone_number, 'comments': comment})
        return phonebook