numero = int(input('Digite um número Natural menor que 1000: '))

unidade = numero % 10

x = (numero - unidade)/10
dezena = x % 10

y = (x - dezena)/10
centena = y % 10

dezena = int(dezena)
centena = int(centena)

print('O número possui', centena,'centena(s)',dezena,'dezena(s)',unidade,'unidade(s)')



