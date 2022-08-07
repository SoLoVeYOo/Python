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