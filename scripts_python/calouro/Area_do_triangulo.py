a = int(input('Digite uma hipotenusa: '))
b = int(input('Digite um cateto: '))

def cat2 (a, b):
    return  ((a**2-b**2)**(1/2))

def area (a, b):
    return (cat2(a, b)*b)/2
    
print(area(a, b))