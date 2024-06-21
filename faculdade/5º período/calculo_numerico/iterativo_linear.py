# Eq: x^3 - 9x + 5 = 0
# x^3 + 5 = 9x
# psi 1: x = (x^3 + 5)/9  

ERRO = 10e-8
INTERVALO_INFERIOR = 0.5
INTERVALO_SUPERIOR = 1

def psi(x):
    return (x**3 + 5)/9

def func(x):
    return x**3 - 9*x + 5

chute = (INTERVALO_INFERIOR + INTERVALO_SUPERIOR)/2

while True:
    if (abs(func(psi(chute))) < ERRO):
        print(f"chute: {chute}\n valor de f(chute): {func(psi(chute))}\n")
        break

    chute = psi(chute)