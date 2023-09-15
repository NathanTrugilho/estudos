a = int(input('Digite um número: '))
b = int(input('Digite um número: '))

def MaiorOuMenor(a, b):
    if a > b:
        print('a é maior do que b')
    else:
        print('a é menor do que b')
    return(a, b)
print(MaiorOuMenor(a, b))
