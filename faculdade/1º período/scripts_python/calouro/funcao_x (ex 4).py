x = float(input('Digite um numero: '))

def funcao(x):
    if x <= 1:
        return (4*x)
    elif x > 1 and x <= 2:
        return (8*(x**2)-20*x+16)
    elif x > 2 and x < 5:
        return (x**3-10*x**2+32.25*x-24.5)
    elif x >= 5 and x <= 7:
        return (13)
    elif x > 7:
        return (-x+20)

print(funcao(x))
