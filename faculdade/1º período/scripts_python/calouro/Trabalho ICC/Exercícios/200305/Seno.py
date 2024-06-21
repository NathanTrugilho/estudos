import math

def seno(x):

    inverte = 1
    soma = 0

    for n in range(3, 21, 2):

        if (inverte%2) == 0:
            soma = soma + (x**n) / math.factorial(n)
        else:
            soma = soma - (x**n) / math.factorial(n)

        inverte = inverte + 1

    return x + soma

x = int(input('Digite um numero: '))
print(seno(x))
