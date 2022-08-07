from module_converting import converting as con
from module_calculation import decision as dec
from logger import log
import view

def buttom_click():
    nickname = view.name_person()
    primer = view.get_primer()
    try:
        result = con(primer)
        result = dec(result)
        log(nickname, primer, result)
        view.view_result(primer, result)
    except:
        print('Выражение введено с ошибками. Запустите программу заного и введите, пожалуйста, выражение верно.')
        log(nickname, primer, 'Выражение было введено с ошибками.')
        exit()