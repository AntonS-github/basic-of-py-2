import add_student as add
import search_student as search
import del_student as cut
import init_logs

def switch():
    ask = input('Выберите режим работы добавление пользователя (a), поиск (s) или удаление (d): ')
    if ask == 'a':
        init_logs.new_log(add.get_input(), 'a')
    elif ask == 's':
        init_logs.new_log(search.searching(), 's')
    elif ask == 'd':
        init_logs.new_log(cut.del_student(), 'd')
    else:
        print('Некорректный ввод')


