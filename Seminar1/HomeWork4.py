# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).


def int_input(message):
    str1 = input(message)
    if str1.isdigit():
        result = int(str1)
    else:
        print('Введено не число')
        result = -1
    return result

while True:
    n = int_input('Введите номер четверти на плоскости (0 - выход]): ')
    if n == 0:
        break
    elif n == 1:
        print('x > 0 и y > 0')
    elif n == 2:
        print('x < 0 и y > 0')
    elif n == 3:
        print('x < 0 и y < 0')
    elif n == 4:
        print('x > 0 и y < 0')
    elif n < 1 or n > 4:
        print('Неверное значение')
        
    