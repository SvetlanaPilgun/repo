''' Задача 1
Задана матрица неотрицательных чисел. Посчитать сумму элементов в каждом столбце. Определить, какой столбец содержит максимальную сумму.
'''

file = open('File_2.txt')
N = 0
mass = []
for line in file:
    z = []
    row = line.strip().split('  ')
    for i in range(len(row)):
        z.append(int(row[i]))

    mass.append(z)
    N += 1
file.close()
print ('----------------------------------')

for i in range(len(mass)):
    for j in range(len(mass[i])):
        print("%4d" % mass[i][j], end='')
    print()

print ('----------------------------------')

maxx = 0
column = 0

for i in range(len(mass)):
    s = 0
    for j in range(len(mass[i])):
        s += mass[j][i]
        if maxx < s:
            maxx = s
            column = i+1

    print("%4d" % s, end='')

print()
print(maxx, column)
print()

''' Задача 2
В текстовом файле посчитать количество строк, а также для каждой отдельной строки определить количество в ней символов и слов.
'''

file = open('File_DZ6_2.txt')


for line in file:
    #line = file.readline()
    print (line, end='')
    print ('длина фразы: ', len(line))
    a = line.strip().split(' ')
    print('колво слов: ', len(a))
    print()

file.close()




