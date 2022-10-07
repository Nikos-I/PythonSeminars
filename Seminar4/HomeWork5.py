# 5. Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

import io
from random import randint



# for i in range(1, 2):
#     with io.open(f'polynom{i}.txt', 'r') as f:
#         for line in f:
#             print(line)
            
#         poly_txt = for d_poly in line:

#         k_poly = randint(k_min, k_max)
#         k_sign = '+' if k_poly > 0 else '-'
#         k_poly = abs(k_poly)
#         if k_poly != 0:
#             if d_poly == 0:
#                 tmp_str = f' {k_sign} {k_poly}'
#             elif d_poly == 1:
#                 tmp_str = f'{k_sign} {k_poly}x'
#             elif d_poly == p_degree-1:
#                 tmp_str = f'{k_poly}x**{d_poly} '
#             else:
#                 tmp_str = f'{k_sign} {k_poly}x**{d_poly} '

#         out_str = tmp_str + out_str
    