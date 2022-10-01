# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# (1+(1/n))**n
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}


def int_input(message):
    str1 = input(message)
    try:
        result = int(str1)
    except:
        print('Введено не число')
        result = -1
    finally:
        return result
   

def sequence(n):
    ret_seq = [round((1 + 1 / x)**x, 3) for x in range (1, n + 1)]  
    return ret_seq
        

n = int_input('Введите число: ') 
print(sequence(n))
print(round(sum(sequence(n)),3))


# С семинара

# n = int(input('Введите число: '))
# my_list = [[n, round(((1+1/n)**n),2)] for n in range(1,n+1)]
# print('Последовательность чисел: ', dict(my_list))
# print('Сумма чисел последовательности: ', sum(dict(my_list)))
