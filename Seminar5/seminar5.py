text = 'Съешь ещёабв этих мягабвких французских булок абв'

my_list = list(filter(lambda x: 'абв' not in x , text.split()))

print(' '.join(my_list))


