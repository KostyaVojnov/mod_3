x = int(input('сумма вклада'))
p = int(input('процент'))
y = int(input('желаемая сумма'))

year = 0

while x < y:
    x += (x*p)//100
    year += 1

print(year)




