import math

ERRO = 10e-8
a = 0
b = 1.0

def eq(x):
    return x - math.cos(x)

while True:
    c = b - eq(b)*((b-a))/(eq(b)-eq(a))
    if abs(eq(c)) <= ERRO:
        print(f"\nA raiz aproximada aparece em {c} e tem valor aproximado de {eq(c)}\n")
        break
    print(a)
    print(b)
    print(c)
    print(eq(c))
    print("\n")
    a = b
    b = c