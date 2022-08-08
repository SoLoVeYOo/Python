from slovari import *

def converting (stroka: str) -> list:
    stroka = stroka.replace(' ', '') # позволяет пользователю вводить выражения через пробел
    stroka = stroka.replace(',', '.') # позволяет пользователю вводить вещественные числа как через точку, так и через запятую
    result, temp_str = [], ''
    if stroka[0] == '-': temp_str, stroka = stroka[0], stroka[1:]
    for i in range(len(stroka)):
        if stroka[i].isdigit() == True or stroka[i] == '.': temp_str += stroka[i]
        elif stroka[i] == 'j':
            result.append(complex(0, float(temp_str)))
            temp_str = ''
        elif stroka[i] in skobki:
            if stroka[i] == '(': result.append(stroka[i])
            elif stroka[i] == ')' and len(temp_str) >= 1:
                result.append(float(temp_str))
                result.append(stroka[i])
                temp_str = ''                
            else: result.append(stroka[i])
        elif stroka[i] in operations:
            if stroka[i] == '-' and stroka[i-1] == '(': temp_str += stroka[i]
            elif stroka[i] in operations and (stroka[i-1] == ')' or stroka[i-1] == 'j'): result.append(stroka[i])
            else:
                result.append(float(temp_str))
                result.append(stroka[i])
                temp_str = ''
        else: return 'q'
        if i == len(stroka)-1 and len(temp_str) >= 1: 
            result.append(float(temp_str))
    return result