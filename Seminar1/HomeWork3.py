# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0
# и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
#
# Пример:
#
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3


# Применено try-except потому что у isdigit() проблемы с отрицательными числами (минус - не считается цифрой)
def int_input(message):
    str1 = input(message)
    try:
        result = int(str1)
    except:
        print('Введено не число')
        result = -1
    finally:
        return result


while True:
    X = int_input('Введите координату X (0 - закончить): ')
    Y = int_input('Введите координату Y (0 - закончить): ')
    quarter = 0
    if (X or Y):
        if X == 0:
            print(f"Точка находится на оси X")
        elif Y == 0:
            print(f"Точка находится на оси Y")
        else:
            if X > 0 and Y > 0:
                quarter = 1
            elif X < 0 and Y > 0:
                quarter = 2
            elif X < 0 and Y < 0:
                quarter = 3
            elif X > 0 and Y < 0:
                quarter = 4
            print(f"Точка находится в {quarter} четверти")

    else:
        break
