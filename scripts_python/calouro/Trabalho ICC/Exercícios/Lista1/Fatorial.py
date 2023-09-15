n = int(input('Numero: '))
aux = 1
while n > 1:
    aux = aux * n * (n - 1)
    n -= 2

print('O resultado é:', aux)
