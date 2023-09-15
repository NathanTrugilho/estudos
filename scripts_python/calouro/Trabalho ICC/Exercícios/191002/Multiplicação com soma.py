def multi():
    x = int(input('digite um numero: '))
    y = int(input('digite outro numero: '))

    aux = y
    while 1 < x:
        x -= 1
        aux += y

    return aux

print(multi())








