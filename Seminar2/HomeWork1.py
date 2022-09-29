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
