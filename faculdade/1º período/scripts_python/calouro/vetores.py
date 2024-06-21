from random import randint

qtd = 0
i = 0

lista = []

while i < 50:
    i += 1

    x = randint(0, 20)
    lista.append(x)


for n in range(0, 50):
    y = lista[0 + n]

    if y == 9:
        qtd += 1

print(lista)

print('quantidade', qtd)

#letra a
print('soma', sum(lista))

#letra C
print('maximo', max(lista))

for n in range(0, 50):
    y = lista[0 + n]

    if y == 9:
        print('essa e a posicao do 9:', lista.index(9))
        lista[lista.index(9)] = 0
