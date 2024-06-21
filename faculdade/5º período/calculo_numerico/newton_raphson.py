DELTA = 10e-16
ERRO = 10e-16
X0 = 2

def f(x):
    return x**3 - 2*x - 5

def df(x):
    return (f(x + DELTA) - f(x))/DELTA

x = ( X0 - f(X0)/df(X0))

while True:
     
    if abs(f(x)) <= ERRO:
        print(f"\nA raiz aproximada aparece em {x} e tem valor aproximado de {f(x)}\n")
        break

    x = (x - f(x)/df(x))