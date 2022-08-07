from slovari import operations

def converting (stroka: str) -> list:
    result, temp_str = [], ''
    if stroka[0] == '-': temp_str, stroka = '-', stroka[1:]
    for i in range(len(stroka)):
        if stroka[i].isdigit() == True or stroka[i] == '.': temp_str += stroka[i]
        elif stroka[i] in operations:
            result.append(float(temp_str))
            result.append(stroka[i])
            temp_str = ''
        if i+1 == len(stroka): result.append(float(temp_str))
    return result