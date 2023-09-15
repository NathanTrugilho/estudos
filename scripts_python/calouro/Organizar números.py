#Para fazer com que o programa peça para parar de digitar mais um número, digite 0
x = 1
lista = []
while x != 0:
    n = int(input('Digite alguns números: '))
    if n == 0:
        x = 0
    if n != 0:
        lista.append(n)
print(max(lista), 'é o maior numero')
print(min(lista), 'é o menor numero')

