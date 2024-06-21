a = int(input('Digite um número: '))
b = int(input('Digite um número: '))

def igualdade(a, b):
    if a == b:
        print(a, 'é igual a', b)
    else:
        print(a, 'é diferente de', b)
    return(a, b)
print(igualdade(a, b))
