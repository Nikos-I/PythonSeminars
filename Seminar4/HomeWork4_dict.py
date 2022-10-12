# 4. Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# 20:15

# Выходные файлы сформированы с прицелом на ДЗ5

import io
from random import randint

KOEFF_MIN = -10
KOEFF_MAX = 10
NUM_STEPS = 2


def int_input(message):
    str1 = input(message)
    if str1.isdigit():
        result = int(str1)
    else:
        print('Введено не число')
        result = -1
    return result


def polinom_list(p_degree, k_min, k_max):
    out_list = []
    for d_poly in range(p_degree+1):
        k_poly = randint(k_min, k_max)
        if k_poly != 0:
            out_list.insert(0, [d_poly, k_poly])
    return dict(out_list)


polynom_degree = 5
# polynom_degree = int_input('Введите степень многочлена: ')
for i in range(1, NUM_STEPS+1):
    with io.open(f'polynom_text{i}.txt', 'w') as f:
        print(polinom_list(polynom_degree, KOEFF_MIN, KOEFF_MAX), file=f)

for i in range(1, NUM_STEPS+1):
    with io.open(f'polynom_text{i}.txt', 'r') as f:
        for line in f:
            print(line)
    
    
