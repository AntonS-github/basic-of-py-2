'''
1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
2. Создайте программу для игры с конфетами человек против человека.
Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
a) Добавьте игру против бота
b) Подумайте как наделить бота ""интеллектом""

3. Создайте программу для игры в ""Крестики-нолики"".

4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
Входные и выходные данные хранятся в отдельных текстовых файлах.'''

# Задача 1
# text = 'Шлабва Сашабва по шосабвсе и сосабвала сушку'
# def str_del(text):
#
#     text = list(filter(lambda x: 'абв' not in x, text.split()))
#     return ' '.join(text)
# print(str_del(text))


# Задача 2 конфеты

# None


# Задача 3 крестики и нолики
# def tictactoe():
#     matrix = [['_' for y in range(3)] for x in range(3)]
#     print(matrix)
#     for im in range(3):
#         print(matrix[im])
#     flag = True
#     while flag:
#         cross = input('Игрок-1 введите координаты Х в формете "x y": ').split()
#         x1, y1 = int(cross[0]), int(cross[1])
#         matrix[x1-1][y1-1] = 'X'
#         for im in range(3):
#             print(matrix[im])
#             col = [string[im] for string in matrix]  # columns
#             diag_r = [matrix[i][i] for i in range(3)]  # diagonal right
#             diag_l = [matrix[2-i][i] for i in range(3)]  # diagonal left
#             if len(list(set(matrix[im]))) == 1 and matrix[im][0] != '_':
#                 print(f'Победили {matrix[im][0]}!')
#                 flag = False
#                 break
#             elif len(list(set(col))) == 1 and col[0] != '_':
#                 print(f'Победили {col[0]}!')
#                 flag = False
#                 break
#             elif len(list(set(diag_r))) == 1 and diag_r[0] != '_':
#                 print(f'Победили {diag_r[0]}!')
#                 flag = False
#                 break
#             elif len(list(set(diag_l))) == 1 and diag_l[0] != '_':
#                 print(f'Победили {diag_l[0]}!')
#                 flag = False
#                 break
#
#         nought = input('Игрок-2 введите координаты O в формете "x y": ').split()
#         x2, y2 = int(nought[0]), int(nought[1])
#         matrix[x2-1][y2-1] = 'O'
#         for im in range(3):
#             print(matrix[im])
#             col = [string[im] for string in matrix]  # columns
#             diag_r = [matrix[i][i] for i in range(3)]  # diagonal right
#             diag_l = [matrix[2-i][i] for i in range(3)]  # diagonal left
#             if len(list(set(matrix[im]))) == 1 and matrix[im][0] != '_':
#                 print(f'Победили {matrix[im][0]}!')
#                 flag = False
#                 break
#             elif len(list(set(col))) == 1 and col[0] != '_':
#                 print(f'Победили {col[0]}!')
#                 flag = False
#                 break
#             elif len(list(set(diag_r))) == 1 and diag_r[0] != '_':
#                 print(f'Победили {diag_r[0]}!')
#                 flag = False
#                 break
#             elif len(list(set(diag_l))) == 1 and diag_l[0] != '_':
#                 print(f'Победили {diag_l[0]}!')
#                 flag = False
#                 break
# tictactoe()

# Задача 4 rle

# with open('les5_RLE_decoded.txt', 'r') as data:
#     decoded_text = data.read()
#
#
# def encoding_rle(some_text):
#     str_code = ''
#     prev_el = ''
#     count = 1
#     for el in some_text:
#         if el != prev_el:
#             if prev_el:
#                 str_code += str(count) + prev_el
#             count = 1
#             prev_el = el
#         else:
#             count += 1
#     else:
#         str_code += str(count) + prev_el
#     return str_code
#
#
# str_code = encoding_rle(decoded_text)
# print(str_code)
#
# with open('les5_RLE_encoded.txt', 'r') as data:
#     encoded_text = data.read()
#
#
# def decoding_rle(some_text):
#     count = ''
#     str_decode = ''
#     for el in some_text:
#         if el.isdigit():
#             count += el
#         else:
#             str_decode += el * int(count)
#             count = ''
#     return str_decode
#
#
# str_decode = decoding_rle(encoded_text)
# print(str_decode)
