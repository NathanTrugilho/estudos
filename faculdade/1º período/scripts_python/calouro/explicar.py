#crio a funcao serie que recebe como entrada a quantidade de termos que a serie calculara
def serie(termos):

    #variaveis auxiliares do codigo ('soma_h' guarda a soma total da serie) ('j' e usado para determinar o sinal do proximo termo)
    soma_h = 0
    j = 1

    #cria uma repeticao que vai do primeiro termo ate o ultimo (ultimo termo sera o parametro que sera chamado na funcao)
    for i in range (0, termos):

        #faz a soma dos termos com a parte do sinal ('(-1)**i' vai definir o sinal do proximo termo, quando o i e um numero par ele fica positivo, caso contrario, negativo)
        soma_h = soma_h + (-1)**i * 1/j
        
        #incrementa o numero do denominador de dois em dois, como pedido
        j += 2

    #retorna o valor da soma total
    return soma_h

#chamo a funcao com algum valor ('3' nesse caso) e imprime o resultado que foi retornado
print(serie(3))