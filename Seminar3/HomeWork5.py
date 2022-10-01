# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8
# список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


fib1 = 0
fib2 = 1

n = input("Номер элемента ряда Фибоначчи: ")
n = int(n) + 1

fib_list = []
fib_list1 = []
fib_list.append(fib1)
fib_list.append(fib2)
fib_list1.append(fib2)

for i in range(2, n):
    fib1, fib2 = fib2, fib1 + fib2
    fib_list.append(fib2)   
    fib_list1.append(fib2)   

fib_list1.reverse()
fib_list1 = list(map(lambda x: x * -1, fib_list1))
fib_list1.extend(fib_list)

print(fib_list1)    
