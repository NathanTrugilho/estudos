num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))
num3 = int(input('Digite outro numero: '))

aux = 1

if num1 == num2:
    aux += 1
if num1 == num3:
    aux += 1
if num2 == num3:
    aux += 1

if num1 == num2 == num3:
    print('todos os numeros sao iguais')
elif num1 != num2 and num1 != num3 and num2 != num3:
    print('todos os numeros sao diferentes')
else:
    print(aux, 'numeros sao iguais')

