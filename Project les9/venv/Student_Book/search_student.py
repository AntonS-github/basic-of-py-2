import csv


def searching(query):
    request = query
    with open('catalogue.csv', 'r', encoding='utf-8') as f:
        user_data = list(csv.DictReader(f))
        t = True
        for i in user_data:
            if request.lower() in i.values():
                t = False

                return f"Студент:\nФамилия: {i['LastName'].title()}\nИмя: {i['Name'].title()}\nОтчество: {i['Patronym'].title()}\nТелефон: {i['Phone']}\nФакультет: {i['Faculty'].upper()}\nНомер группы: {i['Group']}"
        if t:
            return print('Нет данных на запрошенного студента')


if __name__ == '__main__':
    searching()
