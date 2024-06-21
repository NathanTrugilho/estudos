def media(a, b, c):
    maior = a

    if b > maior:
        maior = b

    if c > maior:
        maior = c

    meio = a

    if meio == maior:

        if b > c:
            meio = b

        else:
            meio = c

    else:

        if meio < b < maior:
            meio = b

        if meio < c < maior:
            meio = c


    return (maior + meio) / 2


a = int(input('Primeiro numero: '))
b = int(input('Segundo numero : '))
c = int(input('Terceiro numero: '))

print(media(a, b, c))
