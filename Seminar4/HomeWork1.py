# 1. Вычислить число c заданной точностью d
# *Пример:*
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

# decimal библиотека

import decimal as d 
import math as m


# from unicodedata import digit

def int_input(message):
    str1 = input(message)
    try:
        result = int(str1)
    except:
        print('Введено не число')
        result = -1
    finally:
        return result
        
def float_input(message):
    str1 = input(message)
    try:
        result = float(str1)
    except:
        print('Введено не число')
        result = -1
    finally:
        return result

accurace = -1

while accurace:
    accurace = int_input('Введите необходимую точность вычисления (0 - выход]): ')
    if accurace ==0:
        break
    d.getcontext().prec = accurace
    input_number = 0.0
    res_val = d.Decimal('0.0')
    input_number = float_input('Введите вещественное число: ')
    if accurace > 1:
        res_val += d.Decimal(m.pi)
        print(f'PI={res_val}')
        res_val = d.Decimal(m.pi) * d.Decimal(input_number)
        print(f'PI*{input_number} = {res_val}')
