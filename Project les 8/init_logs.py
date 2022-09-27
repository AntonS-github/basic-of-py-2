import datetime
import switch as sw

def new_log(func, mode):
    if mode == 'a':
        with open('logs.txt', 'a', encoding='utf-8') as file:
            file.write(f'Внесены новые данные {datetime.datetime.now()}: {func}\n')     #пишем в файл логов строку дата/время "была внесена строка:" и из модуля эдд строку
    elif mode == 's':
        with open('logs.txt', 'a', encoding='utf-8') as file:
            file.write(f'Был осуществлён поиск {datetime.datetime.now()}: {func}\n')
    elif mode == 'd':
        with open('logs.txt', 'a', encoding='utf-8') as file:
            file.write(f'Был удален пользователь {datetime.datetime.now()}: {func}\n')
    else:
        with open('logs.txt', 'a', encoding='utf-8') as file:
            file.write(f'Была попытка некоректного ввода {datetime.datetime.now()}: {func}\n')
