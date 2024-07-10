import os
from pysr import PySRRegressor
import matplotlib.pyplot as plt 
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import pandas as pd

ARQUIVO_TREINO = "treino.csv"
ARQUIVO_VALIDACAO = "validacao.csv"
ARQUIVO_TESTE = "cofre/teste.csv"
EQUACOES_PKL = "equacoes.pkl"
EQUACOES_CSV = "equacoes.csv"
HORA = 3600
INF = 100000000000

def pausa_tela():
    input("Pressione 'Enter' para continuar...")

def Pysr():        
                                                                                #usecols é para ele carregar apenas as colunas que quero
    arr = np.loadtxt(ARQUIVO_TREINO, delimiter = ',' , dtype = float, skiprows=1, usecols=[1,2,3,5,6,7,9]) 
    xVector = arr[ : ,  [0, 1, 2, 3, 4, 5]] #B, C, D, F, G, H         #skiprows é pra pular a primeira linha (que informa o que é aquele dado) -> transit, fast transit...
    yVector = arr[ : , 6] # J
                                                           
    # Configurações do Pysr ====================================================================== 
    modelo = PySRRegressor(
        model_selection="best",
        niterations=INF,  # Botei um número bem alto para a condição de parada ser dada apenas pelo tempo
        binary_operators=["+", "*", "-", "/", "^"],
        progress=True,
        # A condição de parada ====
        timeout_in_seconds=6*HORA,
        populations=100,
        population_size=100,
        maxsize=30,
        maxdepth=10,
        unary_operators=[
            "sin",
            "cos",
            "exp",
            "log",
            "sinh",
            "cosh",
            "erf",
        ],
        # Faz com que o pysr rode a partir de um progresso já feito
        warm_start=True,
        turbo=True,
        weight_randomize=0.1,
        # Usar se tiver mais de 1000 pontos
        batching=True,
        nested_constraints={"sin": {"sin": 1, "cos": 1, "sinh": 1, "cosh": 1, "erf": 1, "log": 1}, "cos": {"sin": 1, "cos": 1, "sinh": 1, "cosh": 1, "erf": 1, "log": 1},
                            "sinh": {"sin": 1, "cos": 1, "sinh": 1, "cosh": 1, "erf": 1, "log": 1}, "cosh": {"sin": 1, "cos": 1, "sinh": 1, "cosh": 1, "erf": 1, "log": 1},
                            "erf": {"sin": 1, "cos": 1, "sinh": 1, "cosh": 1, "erf": 1, "log": 1}, "log": {"sin": 1, "cos": 1, "sinh": 1, "cosh": 1, "erf": 1, "log": 1}},
        constraints={"^": (9, 1)},
        complexity_of_operators={"/": 3, "exp": 3},
        loss="loss(prediction, target) = (prediction - target)^2", # MSE (erro quadrático médio)
        early_stop_condition="f(loss, complexity) = (loss < 0.000001) && (complexity < 10)",
        equation_file="equacoes.csv",
    )
    modelo.fit(xVector, yVector)
    print(modelo)

def plota_grafico():      
    # Carrego os dados da planilha                                                       
                                                                                # usecols é para ele carregar apenas as colunas que quero
    arr = np.loadtxt(ARQUIVO_TESTE, delimiter = ',' , dtype = float, skiprows=1, usecols=[1,2,3,5,6,7,9]) 
    xVector = arr[ : ,  [0, 1, 2, 3, 4, 5]] #B, C, D, F, G, H         # skiprows é pra pular a primeira linha (que informa o que é aquele dado) -> transit, fast transit...
    yVector = arr[ : , 6] # J
    
    # Inicializo o vetor
    valores_predicao = []

    # Carrego o modelo já existente para a variável "model"
    modelo = PySRRegressor.from_file(EQUACOES_PKL)

    # Faço a contagem das equações
    quantidade_equacoes = int(modelo.equations_.count()["equation"])

    while True:
        # Limpa o array
        valores_predicao = []
        while True:
            os.system('clear')
            print("+---------------------------------------------------------+")
            print("|                  O Regressor simbólico                  |")
            print("+---------------------------------------------------------+")
            print("|-> Escolha a equação de predição gerada pelo PySR        |")
            print("|-> As equações estão ordenadas por complexidade          |")
            print("|-> Deixe em branco e pressione Enter para usar a equação |")
            print("|  escolhida pelo PySR com base na sua seleção de modelo  |")
            print("+---------------------------------------------------------+\n")

            print(f"Encontrei {quantidade_equacoes} equações")
            string_numero_equacao = (input(f"-> Selecione a equação e pressione Enter (0 para voltar): "))

            # Escolhe qual equação será plotada
            if string_numero_equacao == "":
                valores_predicao = modelo.predict(xVector)
                equacao = PySRRegressor.sympy(modelo)
                break
            
            numero_equacao = int(string_numero_equacao)
            numero_equacao -= 1
            
            if numero_equacao == -1:
                return
            
            elif numero_equacao >= 0 and numero_equacao < quantidade_equacoes:
                valores_predicao = modelo.predict(xVector, numero_equacao)
                equacao = PySRRegressor.sympy(modelo, numero_equacao)
                break

            else:
                print("Essa equação não existe!")
                pausa_tela()
        
        # Ordena os valores em ordem crescente
        valores_ordenados = sorted(zip(yVector, valores_predicao))
        valores_reais_ordenados = [v[0] for v in valores_ordenados]
        valores_predicao_ordenados = [v[1] for v in valores_ordenados]

        plt.plot(np.arange(len(yVector)), valores_reais_ordenados, color='blue', marker='o', markersize=8, alpha=1, linestyle='None', label='Valor real do MDO (m³/h)')
        plt.plot(np.arange(len(valores_predicao)), valores_predicao_ordenados, color='red', marker='o', markersize=7, alpha=1, linestyle='None', label='Predição pela eq gerada')

        plt.title('Comparação entre Valor do MDO(m³/h) e Predição pelo PySR')
        plt.xlabel('Índice dos Pontos')
        plt.ylabel('MDO')

        plt.legend()
        print(f'\nEquação escolhida simplificada: {equacao}')
        plt.show()

def observa_metricas():
    # Carrego os dados da planilha
                                                                                    #usecols é para ele carregar apenas as colunas que quero
    arr = np.loadtxt(ARQUIVO_TESTE, delimiter = ',' , dtype = float, skiprows=1, usecols=[1,2,3,5,6,7,9]) 
    xVector = arr[ : ,  [0, 1, 2, 3, 4, 5]] #B, C, D, F, G, H               #skiprows é pra pular a primeira linha (que informa o que é aquele dado) -> transit, fast transit...
    yVector = arr[ : , 6] # J

    modelo = PySRRegressor.from_file(EQUACOES_PKL)

    dicionario_mse = {}
    dicionario_rmse = {}
    dicionario_mae = {}
    dicionario_r2 = {}

    # Faço a contagem das equações
    quantidade_equacoes = int(modelo.equations_.count()["equation"])

    print("") #pular linha

    calcula_mse_geral(dicionario_mse, quantidade_equacoes, modelo, xVector, yVector)

    calcula_rmse_geral(dicionario_rmse, quantidade_equacoes, modelo, xVector, yVector)

    calcula_mae_geral(dicionario_mae, quantidade_equacoes, modelo, xVector, yVector)

    calcula_r2_geral(dicionario_r2, quantidade_equacoes, modelo, xVector, yVector)

    dados = {
        'Equações': list(PySRRegressor.sympy(modelo, i) for i in range (0, quantidade_equacoes)),
        'MSE': list(dicionario_mse.values()),
        'RMSE': list(dicionario_rmse.values()),
        'MAE': list(dicionario_mae.values()),
        'R2': list(dicionario_r2.values())
    }

    df = pd.DataFrame(dados)

    # Crio o arquivo do tipo excel
    df.to_excel('metricas_equacoes.xlsx', index=False)
    pausa_tela()

def calcula_mse_geral(dicionario_mse, quantidade_equacoes, modelo, xVector, yVector):
    
    # Calculo o MSE de todas as equações e guardo num dicionário
    for i in range(1, quantidade_equacoes + 1):

        valores_predicao = modelo.predict(xVector, i - 1)
        mse = mean_squared_error(yVector, valores_predicao)
        dicionario_mse[f"Eq{i}:"] = mse

    # Digo que a primeira chave tem o menor valor de MSE
    chave_menor_valor = next(iter(dicionario_mse.keys()))
    menor_valor = dicionario_mse[chave_menor_valor]
    
    for chave, valor in dicionario_mse.items():
        #print(chave, valor)
        if valor < menor_valor:
            chave_menor_valor = chave
            menor_valor = valor
    
    # Mostro a melhor equação (com menor MSE)
    print(f"A {chave_menor_valor} tem o menor MSE com o valor de: {dicionario_mse[chave_menor_valor]}\n")

def calcula_rmse_geral(dicionario_rmse, quantidade_equacoes, modelo, xVector, yVector):
    
    # Calculo o RMSE de todas as equações e guardo num dicionário
    for i in range(1, quantidade_equacoes + 1):

        valores_predicao = modelo.predict(xVector, i - 1)
        rmse = np.sqrt(mean_squared_error(yVector, valores_predicao)) # Tiro a raiz quadrada do MSE
        dicionario_rmse[f"Eq{i}:"] = rmse

    # Digo que a primeira chave tem o menor valor de RMSE
    chave_menor_valor = next(iter(dicionario_rmse.keys()))
    menor_valor = dicionario_rmse[chave_menor_valor]
    
    for chave, valor in dicionario_rmse.items():
        #print(chave, valor)
        if valor < menor_valor:
            chave_menor_valor = chave
            menor_valor = valor
    
    # Mostro a melhor equação (com menor RMSE)
    print(f"A {chave_menor_valor} tem o menor RMSE com o valor de: {dicionario_rmse[chave_menor_valor]}\n")

def calcula_mae_geral(dicionario_mae, quantidade_equacoes, modelo, xVector, yVector):
    
    # Calculo o MAE de todas as equações e guardo num dicionário
    for i in range(1, quantidade_equacoes + 1):

        valores_predicao = modelo.predict(xVector, i - 1)
        mae = mean_absolute_error(yVector, valores_predicao)
        dicionario_mae[f"Eq{i}:"] = mae

    # Digo que a primeira chave tem o menor valor de MAE
    chave_menor_valor = next(iter(dicionario_mae.keys()))
    menor_valor = dicionario_mae[chave_menor_valor]
    
    for chave, valor in dicionario_mae.items():
        #print(chave, valor)
        if valor < menor_valor:
            chave_menor_valor = chave
            menor_valor = valor
    
    # Mostro a melhor equação (com menor MAE)
    print(f"A {chave_menor_valor} tem o menor MAE com o valor de: {dicionario_mae[chave_menor_valor]}\n")

def calcula_r2_geral(dicionario_r2, quantidade_equacoes, modelo, xVector, yVector):

    # Calculo o R2 de todas as equações e guardo num dicionário
    for i in range(1, quantidade_equacoes + 1):

        valores_predicao = modelo.predict(xVector, i - 1)
        r2 = r2_score(yVector, valores_predicao)
        dicionario_r2[f"Eq{i}:"] = r2

    # Digo que a primeira chave tem o menor valor de R2
    chave_maior_valor = next(iter(dicionario_r2.keys()))
    maior_valor = dicionario_r2[chave_maior_valor]

    for chave, valor in dicionario_r2.items():
        #print(chave, valor)
        if valor > maior_valor:
            chave_maior_valor = chave
            maior_valor = valor

    # Mostro a melhor equação (com menor R2)
    print(f"A {chave_maior_valor} tem o maior R2 com o valor de: {dicionario_r2[chave_maior_valor]}\n")