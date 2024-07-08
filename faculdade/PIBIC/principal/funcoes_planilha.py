import pandas as pd

NOME_ARQUIVO_TRATAMENTO = 'dados.csv'

def filtra_dados(arquivo_entrada):

    nome_planilha = 'Dados Completos (2)'

    planilha = pd.read_excel(arquivo_entrada, sheet_name=nome_planilha)

    # Valores desejados para filtragem
    valores_desejados = ['Eco Transit', 'Fast Transit', 'Transit']

    # Filtrar as linhas onde a primeira coluna contém os valores desejados
    planilha_filtrado = planilha[planilha.iloc[:, 0].isin(valores_desejados)]

    # Salvar o resultado em um arquivo .CSV
    planilha_filtrado.to_csv(NOME_ARQUIVO_TRATAMENTO, index=False)

    print(f'Planilha {nome_planilha} filtrada!')

def dividir_csv():
    
    # Nome dos arquivos de saída
    arquivo_treino = 'treino.csv'
    arquivo_validacao = 'validacao.csv'
    arquivo_teste = 'teste.csv'
    
    planilha = pd.read_csv(NOME_ARQUIVO_TRATAMENTO)

    # Embaralhar as linhas da planilha para dividir
    planilha_embaralhado = planilha.sample(frac=1).reset_index(drop=True)

    # Calcular o número de linhas para cada arquivo (70% treino, 10% validação, 20% teste)
    total_linhas = len(planilha_embaralhado)
    treino_size = int(total_linhas * 0.7)
    validacao_size = int(total_linhas * 0.1)

    planilha_treino = planilha_embaralhado[:treino_size]
    planilha_validacao = planilha_embaralhado[treino_size:treino_size + validacao_size]
    planilha_teste = planilha_embaralhado[treino_size + validacao_size:]

    # Salva as planilhas em 3 arquivos
    planilha_treino.to_csv(arquivo_treino, index=False)
    planilha_validacao.to_csv(arquivo_validacao, index=False)
    planilha_teste.to_csv(arquivo_teste, index=False)

    print(f'Arquivo de treino salvo como {arquivo_treino}')
    print(f'Arquivo de validação salvo como {arquivo_validacao}')
    print(f'Arquivo de teste salvo como {arquivo_teste}')




#Arquivo Excel que vou abrir para filtrar
arquivo_entrada = '/Users/Nathan/Desktop/Dados Isabella para ML 2024.xlsx' 

#filtra_dados(arquivo_entrada)
#dividir_csv()