import csv


def get_input(answer):
    raw_list = answer.split(',')
    student_name = raw_list[0].lower()
    phone = raw_list[1].lower()
    faculty = raw_list[2].lower()
    group = raw_list[3].lower()
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
