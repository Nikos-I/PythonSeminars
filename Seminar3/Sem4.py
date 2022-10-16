
# Задайте строку из набора чисел. 
# Напишите программу, которая покажет большее и меньшее число. 
# В качестве символа-разделителя используйте пробел.

my_list = []

my_list = input('Введите числа через пробел').split()

res_list = [int(elem) for elem in my_list if elem.isdigit()]

val_min = min(res_list)
val_max = max(res_list)

print(f'max = {val_max}, min = {val_min}')



