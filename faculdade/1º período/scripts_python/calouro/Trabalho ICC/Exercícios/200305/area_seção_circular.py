from cmath import pi


a = float(input('Digite um angulo: '))
b = float(input('Digite um raio: '))

def area_setor(a, b):
    return (pi*(b**2)*a)/360

print(area_setor(a, b))
