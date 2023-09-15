def mult(x):
    if (x % 3) == 0:
        return 1
    else:
        return 0
    
x = int(input("Digite um numero: "))
if mult(x):
    print("É multiplo")
else:
    print("Não é multiplo")

