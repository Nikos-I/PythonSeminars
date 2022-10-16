# 5. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

import io
from sympy import *

NUM_STEPS = 2

str_sum = ''
list_source = []

for i in range(1, NUM_STEPS+1):
    with io.open(f'polynom_text{i}.txt', 'r') as f:
        list_source.append(f.readline()[:-1])

str_sum = simplify(list_source[0] + ' + (' + list_source[1] + ')')
f_out = io.open('polynom_sum.txt', 'w')
print(str_sum, file=f_out)
f_out.close()