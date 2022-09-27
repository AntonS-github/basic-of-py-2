from txt_input import txt_input


def search(user_list):
    request = input('Введите запрос по студенту (фамилия, имя или телефон): ').title()
    # user_list = [{'LastName': 'Семенов', 'Name': 'Семен', 'Number': '+734567'}, {'LastName': 'Матвеев', 'Name': 'Матвей', 'Number': '+756789'}, {'LastName': 'Сидоров', 'Name': 'Дмитрий', 'Number': '+712377'}, {'LastName': 'Григорьев', 'Name': 'Станислав', 'Number': '+79987'}]
    t = True
    for i in user_list:
        if i['LastName'] == request or i['Name'] == request or i['Number'] == request:
            print(*i.values())
            t = False
    if t:
        print('Нет такого студента')
in_file = txt_input('data.txt')
search(in_file)
