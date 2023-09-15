a = int(input('Digite um cateto: '))
b = int(input('Digite outro cateto: '))

def hip(a):
    return ((a**2+b**2)**(1/2))
print(hip(a))
