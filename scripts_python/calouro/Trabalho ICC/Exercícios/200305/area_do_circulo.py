from cmath import pi


r = float(input('Escreva um raio: '))

def area_circulo(r):
    return pi*(r**2)
    
print(area_circulo(r))