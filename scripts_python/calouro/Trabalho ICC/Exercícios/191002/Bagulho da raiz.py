import math

numero = float(input('Digite o número para se calcular a raiz: '))

if numero >= 0:
    print(math.sqrt(numero))
else:
    print(math.sqrt(numero*(-1)),'i')
