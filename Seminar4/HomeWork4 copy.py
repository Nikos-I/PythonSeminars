# 4. Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# 20:15

import io
from random import randint

KOEFF_MIN = -10
KOEFF_MAX = 10
NUM_STEPS = 24


def int_input(message):
    str1 = input(message)
    if str1.isdigit():
        result = int(str1)
    else:
        print('Введено не число')
        result = -1
    return result


def polinom_formula(p_degree, k_min, k_max):
    out_str = ''
    k_sign = ''
    for d_poly in range(p_degree):
        k_poly = randint(k_min, k_max)
        k_sign = '+' if k_poly > 0 else '-'
        k_poly = abs(k_poly)
        if k_poly != 0:
            if d_poly == 0:
                tmp_str = f' {k_sign} {k_poly}'
            elif d_poly == 1:
                tmp_str = f'{k_sign} {k_poly}x'
            elif d_poly == p_degree-1:
                tmp_str = f'{k_poly}x**{d_poly} '
            else:
                tmp_str = f'{k_sign} {k_poly}x**{d_poly} '

        out_str = tmp_str + out_str
    out_str += ' = 0'
    return out_str


polynom_degree = int_input('Введите степень многочлена: ')

with io.open('polynom_text.txt', 'w') as f:
    f.writelines(f'k={polynom_degree}\n')
    for i in range(0, NUM_STEPS):
        print(polinom_formula(polynom_degree, KOEFF_MIN, KOEFF_MAX), file=f)

with io.open('polynom_text.txt', 'r') as f:
    for line in f:
        print(line)
    
    
