from operator import ne
from numexpr

import numexpr as ne


def calc_expression(in_str: str):
    tuple_valid = {'0','1','2','3','4','5','6','7','8','9','(',')','+','-','*','/','.'}
    if  not [s for s in list(in_str) if not (s in tuple_valid)]: 
        return ne.evaluate(in_str)
    else:
        return '' 

input_str = '2*67-12/(2+1)'
result = calc_expression(input_str)
print(result)
