import math

def s_pryam(a,b):
    s = a*b
    return (s)

def s_krug(r):
    import math
    s = math.pi * (r ** 2)
    return (s)

def s_tr(a,b,c):
    import math
    p = (a + b + c) / 2
    s = math.sqrt((p * (p - a) * (p - b) * (p - c)))
    return (s)

figure = str(input("Введите название фигуры = "))
if figure == "треугольник":
        a = float(input("Введите сторону a = "))
        b = float(input("Введите сторону b = "))
        c = float(input("Введите сторону c = "))
        if (a < b + c) and (a > b - c) and (b < a + c) and (b > a - c) and (c < a + b) and (c > a - b):
            print('Площадь треугольникa = %.2f' % s_tr(a,b,c))
        else:
            print('с такими сторонами не существует треугольника')
elif figure == "прямоугольник":
    a = float(input("Введите сторону a = "))
    b = float(input("Введите сторону b = "))
    print('Площадь прямоугольникa = %.2f' % s_pryam(a, b))
elif figure == "круг":
    r = float(input("Введите радиус r = "))
    print('Площадь круга = %.2f' % s_krug(r))
else:
    print('Вы ввели фигню')

