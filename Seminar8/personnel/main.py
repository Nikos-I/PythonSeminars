from global_def import *
from position import *
from department import *
from employee import *

# Начало работы

cont_work = True
print_menu()
while cont_work:
    sel_item = menu_select()
    if sel_item == 'comm_end':
        cont_work = False
    elif sel_item != ERROR_COMM:
        eval(sel_item + '()')
        #  literal_eval(sel_item)
    else:
        print('Неверная команда')

