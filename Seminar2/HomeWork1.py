# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11


import re


def float_input(message):
    str1 = input(message)
    try:
        result = float(str1)
    except:
        print('Введено не число')
        result = -1
    finally:
        return result

number1 = float_input('Введите вещественное число: ')
resStr = str(number1)
sumDigit = 0

for c in resStr:
    if c.isdigit():
        sumDigit += int(c)
print(sumDigit)


# С семинара

# n = input("Введите число = ").replace('.', '').replace('-', '')
# while not n.isdigit():
#     n = input("Введите число = ").replace('.', '').replace('-', '')

# my_sum = 0
# # for i in s:
# #     my_sum += int(i)
# n = list(n)
# print(map(int,n))
# my_sum = sum(list(map(int,n)))
# print(my_sum)

# n = float(input('Введите вещественное число: '))
# sum = 0 
# while not n.is_integer(): 
#         n = n*10 
# while n != 0: 
#     sum += n % 10 
#     n //= 10
