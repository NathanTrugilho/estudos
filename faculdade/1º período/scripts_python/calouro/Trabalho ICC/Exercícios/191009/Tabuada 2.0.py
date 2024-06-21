def tabuada(n):

    resposta = []

    aux = 0

    while aux < 9:

        aux += 1

        resp = aux * n

        resposta.append(resp)
    print(resposta)

n = int(input('digite o numero: '))

tabuada(n)

