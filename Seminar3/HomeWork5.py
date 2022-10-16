# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8
# список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

fib1, fib2 = 1, 1
fib_list = [0]


def int_input(message):
    str1 = input(message)
    if str1.isdigit():
        result = int(str1)
    else:
        print('Введено не число')
        result = -1
    return result


input_number = int_input("Номер элемента ряда Фибоначчи: ")

for i in range(input_number):
    fib_list.append(fib1)
    fib_list.insert(0, fib1 * (-1)**i)
    fib1, fib2 = fib2, fib1+fib2

print(fib_list)
