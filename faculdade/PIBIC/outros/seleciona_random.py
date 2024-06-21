import random
# Comentei tudo para nao ter o risco de rodar sem querer 
'''
nome_arquivo_entrada = "dados_tratados_final_sc.csv"
nome_arquivo_saida = "cofre_dados_teste.csv"

# Abre o arquivo de entrada em modo de leitura 
with open(nome_arquivo_entrada, 'r') as arquivo_entrada:
    # Lê todas as linhas do arquivo de entrada
    linhas = arquivo_entrada.readlines()
    
    # Seleciona aleatoriamente 200 índices de linha
    indices_aleatorios = random.sample(range(len(linhas)), 200)
    
    # Abre o arquivo de saída em modo de escrita ('w')
    with open(nome_arquivo_saida, 'w') as arquivo_saida:
        # Escreve as linhas selecionadas no arquivo de saída
        for indice in indices_aleatorios:
            arquivo_saida.write(linhas[indice])
    
    # Remove as linhas selecionadas do arquivo original
    linhas_restantes = [linha for indice, linha in enumerate(linhas) if indice not in indices_aleatorios]
    
    # Sobrescreve o arquivo original com as linhas restantes
    with open(nome_arquivo_entrada, 'w') as arquivo_entrada:
        arquivo_entrada.writelines(linhas_restantes)

print("As 200 linhas aleatórias foram selecionadas e salvas no arquivo de saída.")
print("As linhas selecionadas foram removidas do arquivo original.")
'''


