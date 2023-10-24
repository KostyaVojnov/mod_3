import json
log = input('Введите логин: ')
pswd = input('Ведите пароль: ')

def register (log, pswd):
    data = {log:pswd}

    #with open('data.json', 'w') as f:
        #json.dump(data, f)

    with open('data.json', 'r') as f:
        data = json.load(f)
    if log not in data.keys():
        print('Пользователь не найден')
    else:
        print('Пользователь найден')

register(log, pswd)