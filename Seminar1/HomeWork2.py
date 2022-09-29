# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
var_val = [0,1]
for x in var_val:
    for y in var_val:
        for z in var_val:
            res1 = (not (x or y or z))
            res2 = ((not x) and (not y) and (not z))
            res = (res1 is res2)
            print(x,y,z, res1, res2, res)
