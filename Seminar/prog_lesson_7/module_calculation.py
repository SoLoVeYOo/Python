from slovari import operations

def calculation(spisok: list):
    for oper in operations:
        while oper in spisok:
            for i in range(len(spisok)):
                prov = False
                if oper == spisok[i]:
                    if oper == '/':
                        try: res = spisok[i-1] / spisok[i+1]
                        except:
                            return 'Ошибка! Деление на 0!'
                    else:    
                        match oper:
                            case '*': res = spisok[i-1] * spisok[i+1]
                            case '-': res = spisok[i-1] - spisok[i+1]
                            case '+': res = spisok[i-1] + spisok[i+1]
                    spisok.insert(i-1, res)
                    del spisok[i]
                    del spisok[i]
                    del spisok[i]
                    prov = True
                if prov == True: break 
        if len(spisok) == 1: break
    return spisok[0]

def open_brackets(spisok: list) -> list:
    while '(' in spisok:
        last = max(loc for loc, val in enumerate(spisok) if val == '(') # находим последние '(' скобки
        first = spisok.index(')', last, len(spisok)) # находим первые ')' скобки в интервале от последних '(' скобок
        temp_spisok = list(spisok[last+1:first]) # создаем временный список с выражением в скобках
        dlina = len(temp_spisok) # длина выражения в скобках
        if calculation(temp_spisok) == 'Ошибка! Деление на 0!':
            spisok = 'Ошибка! Деление на 0!'
            return spisok
        else:
            spisok.insert(last, calculation(temp_spisok)) # добавляем в исходный список результат выражения в скобках
            for _ in range(dlina+2): del spisok[last+1] # удаляем из исходного списка выражение в скобках и сами скобки
    return spisok

def decision(spisok):
    if '(' in spisok: open_brackets(spisok)
    if spisok == 'Ошибка! Деление на 0!': return spisok
    return(calculation(spisok))