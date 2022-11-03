from position import pos_list
from department import pd_list
from global_def import *


def comm_list():    # Список сотрудников
    exec_str = 'select * from empl_full_list'   
    conn, cur = conn_open()
    cur.execute(exec_str)
    list_emploee = list((cur.fetchall()))
    for id, name, dep, pos in list_emploee:
        print(id, name, dep, pos)
    conn.close()


def comm_add_e():
    print('Добавление сотрудника:')
    name = input('Введите Ф.И.О. сотрудника: ')
    pd_list(0)
    id = input('Введите id должности в отделе: ')
    if name:
        conn, cur = conn_open()
        exec_str = f"insert into personnel (c_emploeer, id_depart_pos) values ('{name}', {id});"
        cur.execute(exec_str)
        last_row_id = cur.lastrowid
        conn.commit()
    comm_list()


def comm_del_e():
    print('Удаление сотрудника:')
    comm_list()
    id = input('Введите id сотрудника: ')
    if id:
        conn, cur = conn_open()
        exec_str = f"delete from personnel where id_emploeer = ('{id}');"
        cur.execute(exec_str)
        conn.commit()
    comm_list()
