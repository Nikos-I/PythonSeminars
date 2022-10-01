# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# Пример неверный - мин. дробная часть = 0

my_list = [1.1, 1.2, 3.1, 5.001, 10.01]
frac_min = frac_max = round(my_list[0] % 1, 4)

for i in range(1, len(my_list)):
    cur_val = round(my_list[i] % 1, 4)
    if frac_min > cur_val:
        frac_min = cur_val
    if frac_max < cur_val:
        frac_max = cur_val

print(frac_max-frac_min)
