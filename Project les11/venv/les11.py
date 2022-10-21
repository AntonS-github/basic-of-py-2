# Задача 1
""" MinStat, MaxStat, AverageStat"""
# import statistics
#
#
# class MinStat:
#     mins_list = []
#
#     def __init__(self):
#         self.num = None
#
#     def add_number(self, num):
#         self.num = num
#         self.mins_list.append(self.num)
#         return self.mins_list
#
#     def result(self):
#         return min(self.mins_list)
#
#
# class MaxStat:
#     maxs_list = []
#
#     def __init__(self):
#         self.num = None
#
#     def add_number(self, num):
#         self.num = num
#         self.maxs_list.append(self.num)
#         return self.maxs_list
#
#     def result(self):
#         return max(self.maxs_list)
#
#
# class AverageStat:
#     ave_list = []
#
#     def __init__(self):
#         self.num = None
#
#     def add_number(self, num):
#         self.num = num
#         self.ave_list.append(float(self.num))
#         return self.ave_list
#
#     def result(self):
#         return statistics.mean(self.ave_list)
#
#
# mins = MinStat()
# maxs = MaxStat()
# aves = AverageStat()
# values = [2, 4, 2, 6, 8, 10]
# for i in values:
#     mins.add_number(i)
#     maxs.add_number(i)
#     aves.add_number(i)
# print(mins.result(), maxs.result(), '{:<05.3}'.format(aves.result()))


# Задача 2
''' Sending SMS'''


# class Person:
#     def __init__(self, name, paternity, surname, phone_dict):
#         self.name = name
#         self.paternity = paternity
#         self.surname = surname
#         self.phone_dict = phone_dict
#
#     def get_phone(self):
#         return self.phone_dict.get('private', None)
#
#     def get_name(self):
#         return f'{self.surname} {self.name} {self.paternity}'
#
#     def get_work_phone(self):
#         return self.phone_dict.get('work', None)
#
#     def get_sms_text(self):
#         return f'Уважаемый {self.name} {self.paternity}! Примите участие в нашем беспроигрышном конкурсе!'
#
#
# class Company:
#     def __init__(self, company_name, company_type, com_phone_dict, *args):
#         self.company_name = company_name
#         self.company_type = company_type
#         self.com_phone_dict = com_phone_dict
#         self.person = args
#
#     def get_phone(self, key = 'contact'):
#         if key in self.com_phone_dict:
#             return self.com_phone_dict.get(key)
#         for person in self.person:
#             number = person.get_work_phone()
#             if number:
#                 return number
#
#     def get_name(self):
#         return self.company_name
#
#     def get_sms_text(self):
#         sms = f'Для вашей компании {self.company_name} есть суперпредложение. ' \
#               f'Примите участие в конркусе для {self.company_type}'
#         return sms
#
#
# def sms_send(*args):
#     for arg in args:
#         if arg.get_phone() is not None:
#             print(f'Отправлено SMS на номер {arg.get_phone()}: {arg.get_sms_text()}')
#         else:
#             print(f'Не удалось отправить SMS абоненту {arg.get_name()}')
#
#
# person1 = Person('Ivan', 'Ivanovich', 'Ivanov', {'private': 888, 'work': 999})
# person2 = Person('Petr', 'Ivanovich', 'Petrov', {'private': 888})
# person3 = Person('Michail', 'Petrovich', 'Ionov', {'work': 777})
# com1 = Company('Roga', "AO", {"contact": 7777})
# com2 = Company('XXX', "OOO", {"non_contact": 2626})
# sms_send(person1, person2, person3, com1, com2)
