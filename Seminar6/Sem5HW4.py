from itertools import groupby
import io

# # Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# # *Входные и выходные данные хранятся в отдельных текстовых файлах.*



# def encoding_RLE(seq_in):   # Кодировать строку
#     str_compress = ''
#     count = 1
#     char = seq_in[0]
#     if not seq_in:
#         return
#     for i in range(1, len(seq_in)):
#         if seq_in[i] == char:
#             count += 1
#         else:
#             str_compress += (str(count) + char)
#             char = seq_in[i]
#             count = 1
#     str_compress += (str(count) + char)
#     return str_compress

def encoding_RLE(seq_in):           # Кодировать строку (модифицированный вариант)
    return ''.join([x[0]+x[1] for x in [[str(sum(1 for _ in g)), k] for k,g in groupby(list(seq_in))]])


def file_en_RLE(f_input, f_encode):  # Кодировать файл
    with io.open(f_input, 'r') as f_in:
        with io.open(f_encode, 'w') as f_en:
            for line in f_in:
                f_en.write(encoding_RLE(line.strip('\n'))+'\n')
    return


def decoding_RLE(seq_in):   # Декодировать строку
    str_decompress = ''
    count = ''
    if not seq_in:
        return
    for char in seq_in:
        if char.isdigit():
            count += char
        else:
            str_decompress += char * int(count)
            count = ''
    return str_decompress


def file_de_RLE(f_output, f_encode):  # Декодировать файл
    f_out = io.open(f_output, 'w')
    with io.open(f_encode, 'r') as f_en:
        for line in f_en:
            f_out.write(decoding_RLE(line.strip('\n'))+'\n')
    f_out.close()
    return 0


file_en_RLE('input.txt', 'rle_encode.txt')
file_de_RLE('output.txt', 'rle_encode.txt')

print('Готово! input.txt => rle_encode.txt => output.txt')