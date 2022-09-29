# Реализуйте алгоритм перемешивания списка.


import random


N = 10
res_list = []
for i in range(N):
    res_list.append(random.randint(-N, N))
print(res_list)    
random.shuffle(res_list)
print(res_list)    

