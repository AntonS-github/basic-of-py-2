'''Задача: доделать задачи 41 и 43, причем с применением функций ускоренной обработки данных.

в 41 задаче можно решить вариант без использования скобок.

Задача 41: Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный.

*Пример:*

2+2 => 4;

1+2*3 => 7;

1-2*3 => -5;

- Добавьте возможность использования скобок, меняющих приоритет операций.

    *Пример:*

    1+2*3 => 7;

    (1+2)*3 => 9;


Задача 43: Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
'''

# Задача 43
# initList = [1, 2, 3, 5, 1, 5, 3, 10]
# resultList = []
# for i in range(len(initList)):
#     count = True
#     for j in range(0, i):
#         if initList[i] == initList[j]:
#             count = False
#     for j in range(i+1, len(initList)):
#         if initList[i] == initList[j]:
#             count = False
#     if count:
#         resultList.append(initList[i])
# print(initList)
# print(resultList)

# Задача 41 не сделана!

# get_data = input('Введите выражение: ')
# for i, k in enumerate(get_data):
#     flag = True
#     if k == '*':
#         temp = int(get_data[i-1]) * int(get_data[i+1])
#         flag = False
#         print(temp)
#     elif k == '/':
#         temp = int(get_data[i - 1]) / int(get_data[i + 1])
#         flag = False
#         print(temp)
#     if flag == True and k =='+':
#         res = int(get_data[i - 1]) + int(get_data[i + 1])
#     elif flag == True and k =='-':
#         res = int(get_data[i - 1]) - int(get_data[i + 1])
#     elif flag == False and k =='+':
#         res = int(get_data[i - 1]) + temp
#     elif flag == False and k == '-':
#         res = int(get_data[i - 1]) - temp
# print(res)

#задача про футбол
# Напишите программу, которая принимает на стандартный вход список игр футбольных команд с результатом матча и выводит на стандартный вывод сводную таблицу результатов всех матчей.
#
# За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.
#
# Формат ввода следующий:
# В первой строке указано целое число nn — количество завершенных игр.
# После этого идет nn строк, в которых записаны результаты игры в следующем формате:
# Перваякоманда;Забитопервойкомандой;Втораякоманда;Забитовторойкомандой
#
# Вывод программы необходимо оформить следующим образом:
# Команда:Всегоигр Побед Ничьих Поражений Всегоочков
#
# Конкретный пример ввода-вывода приведён ниже.
#
# Порядок вывода команд произвольный.
#
# Sample Input:
#
# 3
# Спартак;9;Зенит;10
# Локомотив;12;Зенит;3
# Спартак;8;Локомотив;15
# Sample Output:
#
# Спартак:2 0 0 2 0
# Зенит:2 1 0 1 3
# Локомотив:2 2 0 0 6
# num_teams = int(input("Введите количество команд: "))
# teams = []
# wins = {}
# losses = {}
# draws = {}
# for i in range(num_teams):
#     data = input().split(';')
#     if data[0] not in teams:
#         teams.append(data[0])
#     if data[-2] not in teams:
#         teams.append(data[-2])
#     if data[1] > data[-1]:
#         wins[data[0]] = wins.get(data[0], 0) + 1
#         losses[data[-2]] = losses.get(data[-2], 0) + 1
#     elif data[1] < data[-1]:
#         wins[data[-2]] = wins.get(data[-2], 0) + 1
#         losses[data[0]] = losses.get(data[0], 0) + 1
#     else:
#         draws[data[0]] = draws.get(data[0], 0) + 1
#         draws[data[-2]] = draws.get(data[2], 0) + 1
