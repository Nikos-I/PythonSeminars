# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.


import random


N = 7
res_list = []
for i in range(N):
    res_list.append(random.randint(-N, N))
print(res_list)    

res_mul = 1
path = '.\Seminar2\indpos.txt'
data = open(path, 'r')
for line in data:
    res_mul *= res_list[int(line)]
data.close()

print(res_mul)
