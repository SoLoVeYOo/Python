from module_converting import converting as con
from module_calculation import calculation as cal
import view

def buttom_click():
    primer = view.get_primer()
    result = con(primer)
    result = cal(result)
    view.view_result(primer, result)