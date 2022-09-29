# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
import math

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


def coord_input(point_name):
    coord = []
    print('Введите координаты')
    coord.append(int_input(f"{point_name} X: "))
    coord.append(int_input(f"{point_name} Y: "))
    return coord


point_a = coord_input('A')
point_b = coord_input('B')
distance = math.sqrt(math.pow(point_a[0] - point_b[0], 2) + math.pow(point_a[1] - point_b[1], 2))
print(f"{distance:.2f}")
