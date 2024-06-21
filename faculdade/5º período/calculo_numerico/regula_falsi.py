import math
ERRO = 10e-6
a = 0
b = 1

def eq(x):
    return x - math.cos(x)

while True:
    c = b - eq(b)*((b-a))/(eq(b)-eq(a))
    if abs(eq(c)) <= ERRO:
        print(f"\nA raiz aproximada aparece em {c} e tem valor aproximado de {eq(c)}\n")
        break
    print(f"c = {c}\na = {a}\nb = {b}")
    print(eq(c))
    if(eq(a) * eq(c)) > 0:
        a = c
    
    elif(eq(b) * eq(c)) > 0:
        b = c