import math

ERRO = 10e-16
a = 0.0
b = 1.0

def eq(x):
    return x - math.cos(x)

while True:
    if(eq(a) * eq(b)) > 0:
        print("Intervalos incorretos!")
        break

    c = (a + b)/2
    if abs(eq(c)) <= ERRO:
        print(f"\nA raiz aproximada aparece em {c} e tem valor aproximado de {eq(c)}\n")
        break

    if(eq(a) * eq(c)) > 0:
        a = c
    
    elif(eq(b) * eq(c)) > 0:
        b = c

    