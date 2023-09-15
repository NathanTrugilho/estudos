x = int(input('Digite um número: '))


def MaiorPrimo(x):
    n = 1
    while (n <= x):
        n = 1
        n = n + 1
        if (x % 1) == 0 and x != 1:
            return(1)
        else:
            return(0)


print(max(MaiorPrimo(x)))
# criar uma variavel, criar um count com os conjuntos dos numeros naturais.
# dividir n por count,
# se tiver resto zero é pq é multiplo, logo nao é numero primo.
