'''1. Вычислить число c заданной точностью d

2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

5. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

4 или 5 на выбор со звездой'''

# Задача 1
# d = input('Введите точность вычислений: ')les5
# a = float(input('Введите число для вычислений: '))
# accur = len(d.split('.')[1])
# res = round(a, accur)
#
# if len(str(res).split('.')[1]) < accur:
#     print(str(res).join('0'*((accur+1)-len(str(res).split('.')[1]))))
# else:
#     print(res)

# Задача 2
# n = int(input('Введите натуральное число: '))
# i = 2
# out_list = []
# while i * i <= n:
#     while n % i == 0:
#         out_list.append(i)
#         n = n / i
#     i = i + 1
# if n > 1:
#     out_list.append(n)
# print(set(out_list))


# Задача 3
# list = [1, 2, 3, 3, 3, 4, 5, 6, 6, 7, 1, 5, 6, 3, 4]
# print(set(list))

# Задача 4
# import random
# import itertools
#
# k = int(input('Введите степень многочлена: '))
# k_list = [random.randint(0, 100) for _ in range(k)]
# print(k_list)
# def get_polynom(k, k_list):
#     var = ['x^'] * (k - 1) + ['x']
#     polynom = [[a, b, c] for a, b, c in itertools.zip_longest(k_list, var, range(k, 1, -1), fillvalue='') if a != 0]
#     for x in polynom:
#         x.append(' + ')
#     polynom = list(itertools.chain(*polynom))
#     polynom[-1] = ' = 0'
#     return "".join(map(str, polynom)).replace(' 1x', ' x')
#
# poly_1 = get_polynom(k, k_list)
# print(poly_1)
#
# with open('exercise4-4.txt', 'w') as file:
#     file.write(poly_1)

