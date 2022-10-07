# 2. Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.

import math 

NUM = 258

def prime_factors(inp_num): 
    res_list = []
    while inp_num % 2 == 0: 
        res_list.append(2) 
        inp_num = inp_num / 2 
# Каждое составное число имеет хотя бы один простой множитель, 
# меньший или равный квадратному корню.
    for i in range(3, int(math.sqrt(inp_num)) + 1, 2): 
        while inp_num % i == 0: 
            res_list.append(i) 
            inp_num = inp_num / i 
    if inp_num > 2: 
        res_list.append(int(inp_num)) 
    return res_list
 

print(prime_factors(NUM)) 