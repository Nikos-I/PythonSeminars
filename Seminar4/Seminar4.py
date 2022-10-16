text = 'Съешь ещёабв этих мягабвких французских булок абв'

my_list = list(filter(lambda x: 'абв' not in x , text.split()))

print(' '.join(my_list))


# Считаю объяснение задачи с конфетами непонятным как в лекции, так и в семинаре.
# Если кому-то пригодится, могу предложить свой комментарий к задаче:

# Чтобы мне победить, нужно, чтобы к концу игры после моего хода осталось 29 конфет. Тогда соперник возьмет сколько-то конфет (от 1 до 28), и как минимум одна конфета останется для моего последнего победного хода.

# Как обеспечить 29 конфет к концу игры?
# Упростим задачу. Представим, что исходное число конфет делится на 29 без остатка: к примеру, изначально у нас не 2021, как в условии, а 2001 (= 29*69).
# Если от 2001 отнимать каждый раз по 29, то на 68-й раз останется ровно 29 (ведь 2001 делится на 29 без остатка).
# А как нам отнимать каждый раз именно 29? Соперник берет 20, я следом за ним 9 (вместе 29); он берет 19, я 10 (вместе 29); он берет n, я беру (29 – n). То есть я каждый раз «добираю» до 29. К концу игры неизбежно останется 29 конфет.

# Вспоминаем, что у нас исходное число конфет 2021 не делится на 29. Так исправим это – первым ходом отнимем от 2021 то, что «мешает», в нашем случае 20.
# 20 – это ничто иное как остаток от деления 2021 на 29.
# Таким образом, первый ход – забираю количество конфет, равное остатку от деления 2021 на 29. Последующие ходы – см. пункт 2.

# https://gb.ru/chapters/24437

# https://github.com/Puena/GbPython/blob/main/Practice_5/task_2.py
