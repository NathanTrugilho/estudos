a = int(input('Digite três números diferentes: '))
b = int(input('Digite três números diferentes: '))
c = int(input('Digite três números diferentes: '))

def menorNumero(a, b,c):
    if a < b < c:
       print(a, 'é o menor número')
    elif b < a < c:
       print(b, 'é o menor número')
    else:
       print(c, 'é o menor número')
    return (a, b, c)
print(menorNumero(a, b, c))
