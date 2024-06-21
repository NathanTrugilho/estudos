#Tem que usar o int para transformar o 'valor' de string para inteiro.
#Caso não haja o int, os números vão ser interpretados como strings e serão concatenados.

a = int (input ("digite o primeiro numero:"))
b = int (input ("digite o segundo numero:"))

num = a + b

if num > 100:
    print (a + b)
else :
    print ('resultado menor ou igual a 100')
