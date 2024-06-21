y = int(input('digite o número da base: '))
x = int(input('digite o número da potência: '))

aux = y
while 1 < x:
    x -= 1
    aux = aux*y

print(aux)
