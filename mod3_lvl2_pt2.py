from random import randint

n = 5
m = [[randint(0,100) for i in range(n)] for j in range(n)]

def max_element(element):
    max_number = 0
    for i in element:
        for j in i:
            if j > i:
                max_number = j
    print(j)

max_element(m)

