'''
Написать программу, в которой хранятся данные о товарах, их количестве и цене. При запуске программы эта информация выводится на экран.
 Далее пользователю должно предлагаться вводить номера товаров и их новое количество. Изменение данных должно завершаться
 , если пользователь вводит специально оговоренный символ (например, 0). После этого все данные о товарах должны снова выводиться на экран.
'''

file = open('File_DZ5.txt')

sklad = dict()
for tov in file:
    t = tov.strip().split(' ')
    nomer = t[0].strip()
    info = t[1:]
    for i in nomer:
        sklad[i] = info
file.close()
print(sklad)
name = 0
colvo = 1
cost = 2
for i in sklad:
    print("%s. %s - %s шт. по %s грн" % (i, sklad[i][name], int(sklad[i][colvo]), sklad[i][cost]))

while 1:
    n = input('№: ')
    if n != '0':
        count_new = int(input('Количество: '))
        sklad[n][1] = count_new
    else:
        break

for i in sklad:
    print("%s. %s - %s шт. по %s грн" % (i, sklad[i][name], sklad[i][colvo], sklad[i][cost]))
