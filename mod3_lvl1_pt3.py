a = int(input('Введите число:'))
b = int(input('Введите число:'))
c = int(input('Введите число:'))

def area(a, b, c):
    perimeter = a + b + c
    p = (a + b + c) / 2
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print(area)

area(a, b, c)