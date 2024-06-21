def pa():
    an = a1 + (n - 1) * r
    return an


a1 = int(input('digite o primeiro termo'))
r = int(input('digite o valor da razao'))
n = int(input('digite a quantidade de termos da p.a'))

print('o resultado é:', pa())
