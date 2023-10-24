list = [1, 4, 1, 6, 'hello', 'a', 5, 'hello']

new_list =[]

dub_list = []

for i in list:
    if i not in new_list:
        new_list.append(i)
    else:
        dub_list.append(i)
print(new_list, dub_list)