def saraiva():

    inf = 0
    n = 0
    para = 0
    somadiv = 0
    aux = 0
    multiplo = 0
    qtd = 0

    while inf == 0:
        n += 1

        for div in range(1, n):
            if (n % div) == 0:
                somadiv += div

        if somadiv == n:
            print(somadiv)
            para += 1

        somadiv = 0

        if para == 4:
            break

    while aux < n:
        aux += 1

        for i in range(1, aux):
            if aux % i == 0:
                multiplo += 1

        if multiplo == 1:
            qtd += 1
        multiplo = 0

    print('existem', qtd, 'números primos menores que o ultimo numero perfeito')

saraiva()
