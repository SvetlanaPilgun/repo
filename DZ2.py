
a = int(input("Введите коллво строк: "))
d = "^"
p = " "

for i in range(a):    # -------- перебираем строки
    for j in range(2 * a - 1):      # -------- перебираем все символы в строке
        if (a - 1 - i) <= j <= (a - 1 + i):
            print(d, end='')     #рисуем символ не переводя каретки
        else:
            print(p, end='')     #рисуем пробел не переводя каретки
    print()
