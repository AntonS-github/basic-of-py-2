import csv


def get_input():
    student_name = input('Введите ФИО студента через пробел: ').lower()
    phone = input('Введите телефон студента: ').lower()
    faculty = input('Введите факультет студента: ').lower()
    group = input('Введите № группы студента: ').lower()
    fio = student_name.lower().split()
    user_data = [{'LastName': fio[0],
                 'Name': fio[1],
                 'Patronym': fio[2],
                 'Phone': phone,
                 'Faculty': faculty,
                 'Group': group
                 }]
    with open('catalogue.csv', 'r') as f:
        check = f.readlines()
    if len(check) == 0:              # Проверка не пустой ли файл и если пустой, то сразу записываем хэдеры
        writer = csv.DictWriter(f, fieldnames=list(user_data[0].keys()))
        writer.writeheader()
        for i in user_data:
            writer.writerow(i)
    else:
        with open('catalogue.csv', 'a') as f:
            writer = csv.DictWriter(f, fieldnames=list(user_data[0].keys()))
            for i in user_data:
                writer.writerow(i)
    return user_data

if __name__ == '__main__':
    print(get_input())
