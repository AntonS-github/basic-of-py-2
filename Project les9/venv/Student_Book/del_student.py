import csv

def del_student(query):

    request = query
    with open('catalogue.csv', 'r', encoding='utf-8') as f:
        user_data = list(csv.DictReader(f))

    t = True
    for i in user_data:
        if request.lower() in i.values():
            t = False
            buf = i
            print(f"Удалён студент:\nФамилия: {i['LastName'].title()}\nИмя: {i['Name'].title()}\nОтчество: "
                  f"{i['Patronym'].title()}\nТелефон: {i['Phone']}\nФакультет: {i['Faculty'].upper()}\nНомер группы: {i['Group']}")
            user_data.remove(i)
    if t:
        return f'Нет данных на запрошенного студента'
    with open('catalogue.csv', 'w', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=list(user_data[0].keys()))
        writer.writeheader()
        for i in user_data:
            writer.writerow(i)
    return f'{request} успешно удалён из справочника'


if __name__ == '__main__':
    del_student()