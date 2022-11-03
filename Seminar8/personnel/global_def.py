# Общие данные и функции

dict_menu = {
    'list': ['- Список сотрудников\n', 'comm_list'],
    'add_e': ['- Добавить сотрудника', 'comm_add_e'],
    'del_e': ['- Удалить сотрудника\n', 'comm_del_e'],
    'add_p': ['- Добавить должность', 'comm_add_p'],
    'del_p': ['- Удалить должность\n', 'comm_del_p'],
    'add_d': ['- Добавить отдел', 'comm_add_d'],
    'del_d': ['- Удалить отдел\n', 'comm_del_d'],
    'add_pd': ['- Добавить должность в отдел', 'comm_add_pd'],
    'del_pd': ['- Удалить должность из отдела', 'comm_del_pd'] ,
    'end': ['- Завершить работу', 'comm_end'] 
    }

FILE_DB = 'D:/GDisk/GeekBraims/Python/PythonSeminars/Seminar8/personnel/db/personnel.db'
ERROR_COMM = 'Нет такой команды'

conn = None
cur = None

from ast import literal_eval
import operator
from functools import reduce
from sqlite3 import *
import inspect

def print_menu():                               # Печать меню
    global dict_menu

    print('Справочник сотрудников\n\n' +
          'Команды:\n')
    for comm in dict_menu:
        print(comm, dict_menu[comm][0])


def menu_select():  # Выбор пункта меню
    global dict_menu

    comm = input('Введите команду:')
    try:
        func_comm = dict_menu[comm][1]
    except KeyError:
        return ERROR_COMM
    else:
        return func_comm

def conn_open():    # Открыть БД
    conn = connect(FILE_DB)
    curs = conn.cursor()
    return (conn, curs)

def comm_end():
    print('command ', inspect.stack()[0][3])


