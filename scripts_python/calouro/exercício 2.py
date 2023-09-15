from random import randint
numeros_variados = []
i = 0
while i < 10:
    i += 1
    y = randint(0, 20)
    numeros_variados.append(y)

inf = 0
n = 0
aux = numeros_variados[0]
numeros_variados[0] = numeros_variados[9]


while inf < 80:
    bagulho = numeros_variados[n + 1]
    numeros_variados[n + 1] = aux
    n += 1
    aux = bagulho
    inf += 1

    if n == 9:
        n = 0
        print(numeros_variados)
        numeros_variados[0] = numeros_variados[9]
