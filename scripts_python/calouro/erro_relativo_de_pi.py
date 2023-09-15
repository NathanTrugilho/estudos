from math import pi


a = int(input('Digite o raio: '))

valor = 2*pi*a
aproximacao = 6*a

def erro_relativo(a):

    return ((valor - aproximacao)/valor)*100
    
print(erro_relativo(a))