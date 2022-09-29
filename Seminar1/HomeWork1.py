# Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

def int_input(message):
    str1 = input(message)
    if str1.isdigit():
        result = int(str1)
    else:
        print('Введено не число')
        result = -1
    return result


day_number = -1
while day_number:
    day_number = int_input('Введите номер недели (0 - закончить): ')
    if 1 <= day_number <= 7:
        work_days = ['нет', 'нет', 'нет', 'нет', 'нет', 'да', 'да']
        print(f"День № {day_number} выходной? - {work_days[day_number - 1]}")
    elif day_number != 0:
        day_number = -1
