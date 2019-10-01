'''
1. Самое длинное слово в строке
Вводится строка слов, разделенных пробелами. Найти самое длинное слово и вывести его на экран.
Случай, когда самых длинных слов может быть несколько, не обрабатывать.
'''

s = input('Enter something:')
a = s.split()   # без параметра разделителем является пробел
# print (a)  # ----- получили список слов из кот состоит строка
j = 0
max_w = ''
for i in a:
    if len(i) > j:
        j = len(i)
        max_w = i
print('max word is: ', max_w)

'''
2. Удаление лишних пробелов 
Вводится ненормированная строка, у которой могут быть пробелы в начале, в конце и между словами более одного пробела.
Привести ее к нормированному виду, т.е. удалить все пробелы в начале и конце, а между словами оставить только один пробел.
'''

s = input('Enter something:')
a = s.split()
# print(a)
s = str(a)
# print(s)
remove_begin = s.replace("['", "")
# print(remove_begin)
remove_middle = remove_begin.replace("', '", " ")
# print(remove_middle)
remove_end = remove_middle.replace("']", "")
print('Normal record: ', remove_end)
