from random import randint

x = (int(input('Digite um numero: ')))

lista = []
i = 0
while i < 5:
    i += 1
    y = randint(0, x)
    lista.append(y)
print(lista)
print(lista[::-1])
