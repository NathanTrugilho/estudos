n = int(input("Insira a quantidade de elementos que serão impressos: "))

def fibonacci(n):
    termo_1 = 0
    termo_2 = 1
    lista = [termo_1, termo_2]
    
    for i in range(n - 2):
        termo_geral = termo_1 + termo_2
        termo_1 = termo_2
        termo_2 = termo_geral
        lista.append(termo_geral)

    for i in range(n):
        for j in range(n, len(lista)):
            print(lista[j], end=" ")
        print()

fibonacci(n)





