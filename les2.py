'''1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
3. Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
5. Реализуйте алгоритм перемешивания списка.'''

#Задача 1
# n = input('Введите число: ')
# list_n = n.replace('.', '')
# res = sum(map(int, list_n))
# print(res)

#Задача 2
# from random import randint
# res = []
# n = int(input('Введите число элементов: '))
# list_n = [randint(1, 50) for _ in range(n)]
# print(list_n)
# for i in range(n):
#     if i == 0:
#         res.append(list_n[0])
#     elif i > 0:
#         res.append(list_n[i]*list_n[i-1])
# print(tuple(res))

#Задача 3
# N = int(input('Введите число элементов: '))
# list_n = [(1 + 1/n)**n for n in range(1, N)]
# res = sum(list_n)
# print(list_n)
# print(res)

#Задача 4
# from random import randint
# a = []
# n = int(input('Введите число элементов: '))
# list_n = [randint(-n, n) for _ in range(n)]
# print(list_n)
# with open('file.txt', 'w') as file:
#     file.writelines(input('Введите позицию элемента 1: ') + '\n')
#     file.writelines(input('Введите позицию элемента 2: '))
# with open('file.txt', 'r') as file:
#     for i in file.readlines():
#         a.append(i.replace('\n',''))
# res = list_n[int(a[0])] * list_n[int(a[1])]
# print(res)

#Задача 5
# import random
# n = int(input('Введите число элементов: '))
# res = []
# list_n = [random.randint(-n, n) for _ in range(n)]
# print(list_n)
# index_list = [i for i in range(n)]
# print(index_list)
# for i in range(n-1):
#     a = random.choice(index_list)
#     b = random.choice(index_list)
#     list_n[a], list_n[b] = list_n[b], list_n[a]
# print(list_n)