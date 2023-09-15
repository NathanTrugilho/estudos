def conta():
    amigos = int (input ('Quantos amigos estavam presentes?'))
    valor = float (input ('Qual o valor da conta?'))

    x = valor/amigos
    x = 1.1*x
    
    print('O valor que cada um deve pagar é de', x ,'reais')

conta()
