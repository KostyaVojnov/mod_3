d = {'name1': 'id1', 'name2': 'id2', 'name3': 'id3'}

def dict_revers(dict):
    d = {v : k for k, v in dict.items()}
    print(d)


dict_revers(d)