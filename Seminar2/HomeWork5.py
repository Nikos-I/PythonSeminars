# Реализуйте алгоритм перемешивания списка.


import random


N = 10
res_list = []
for i in range(N):
    res_list.append(random.randint(-N, N))
print(res_list)    
random.shuffle(res_list)
print(res_list)    



# С семинара

# import random
# list = [1, 2, 3, 4, 5, 6]
# for i in range(len(list)):
#     a =  random.randint(0,len(list) -1)
#     if list[i] != list[a]:
#         list[i],list[a] = list[a],list[i]
#         print(list[i], list[a])
# print(list)


# a,b = b,a

# import random
# my_list = [1, 2, 3, 4, 5, 6]
# for i, elem in enumerate(my_list):
#     a =  random.randint(0,len(my_list) -1)
#     if elem != my_list[a]:
#         elem,my_list[a] = my_list[a],elem
#         print(elem, my_list[a])
# print(my_list)


# import os
# import random

# # Очистка терминала для удобства восприятия.
# os.system('cls')

# # Реализуйте алгоритм перемещения списка. Без функции shuffle из модуля random

# basic_array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(f'Исходный массив:\n {basic_array}')

# random_array = []
# for i in range(len(basic_array)):
#     random_array.append(basic_array.pop(random.randint(0, len(basic_array)-1)))
# print(f'Перемешанный массив:\n {random_array}')


# my_list = [56, 89, 56, 34, 9, 6]
# new_list =  []
# for _ in (range(len(my_list))):
#     elem = my_list.pop(0)
#     new_list.append(elem)
# print(new_list)

