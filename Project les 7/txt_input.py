def txt_input(file):
    f = open(file, 'r')
    lst_dict = []
    num = f.readlines()
    for i in num:
        raw_test = i.split()
        user_data = {'LastName': raw_test[0],'Name': raw_test[1], 'Number': raw_test[2]}
        lst_dict.append(user_data)
    f.close()
    return lst_dict
