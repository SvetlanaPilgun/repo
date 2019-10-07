
def bin_f(a):
    b = ''
    c = ''
    while a > 0:
        b = bin(a)
        c = b[2:]
        a = 0
    return c


while 1:
    n = int(input('decimal: '))
    if n != 0:
        print('bin: ', bin_f(n))
    else:
        break