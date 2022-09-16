'''1 Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
2 Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
3 Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
4 Напишите программу, которая будет преобразовывать десятичное число в двоичное.

5 Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
]'''

# #Задача 1
# a = []
# for _ in range(int(input('Введите кол-во элементов списка: '))):
#     new_el = int(input('Введите элемент: '))
#     a.append(new_el)
# res = sum([i for i in a[::2]])
# print('Сумма: ', res)


# # Задача 2
# a = []
# new_list = []

# for _ in range(int(input('Введите кол-во элементов списка: '))):
#     new_el = int(input('Введите элемент: '))
#     a.append(new_el)
# if len(a) % 2 != 0:
#     for i in range(int(len(a)/2)+1):
#         if i == 0:
#             mul = a[0]*a[-1]
#             new_list.append(mul)
#         elif a[i] == a[-i]:
#             mul = a[i]**2
#             new_list.append(mul)
#         else:
#             mul = a[i]*a[-(i+1)]
#             new_list.append(mul)
# else:
#     for i in range(int(len(a)/2)):
#         if i == 0:
#             mul = a[0]*a[-1]
#             new_list.append(mul)
#         elif a[i] == a[-i]:
#             mul = a[i]**2
#             new_list.append(mul)
#         else:
#             mul = a[i]*a[-(i+1)]
#             new_list.append(mul)
# print('Произведение: ', new_list)


# Задача 3
# a = []
# new_list = []
# for _ in range(int(input('Введите кол-во элементов списка: '))):
#     new_el = float(input('Введите вещественный элемент: '))
#     a.append(new_el)
# for el in a:
#     k = str(el).split('.')[1]
#     new_list.append(int(k))
# res = max(new_list)-min(new_list)
# print(f'0.{res}')


# Задача 4
# a = int(input('Введите десятиное число: '))
# res = ''
# while a > 0:
#     res = str(a % 2) + res
#     a = a // 2
# print('Двоичное число: ', res)



# Задача 5
# a = int(input("Задайте границы ряда Фибоначчи: "))
# f_list = [0]*(a*2+1)
# f_list[a] = 0
# f_list[a+1] = 1
# for i in range(a+2, len(f_list)):  # в положительную сторону
#     f_list[i] = f_list[i-2]+f_list[i-1]
# for i in range(a, -1, -1):                # в отрицательную сторону
#     f_list[i] = f_list[i+2]-f_list[i+1]
# print(f_list)


