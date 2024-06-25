import os
from pysr import PySRRegressor
import matplotlib.pyplot as plt 
import numpy as np
import sympy as sp
HORA = 3600
INF = 100000000
COLUNA_ARQUIVO_Y = 1
# G2 ^

def pausa_tela():
    input("Pressione 'Enter' para continuar...")

def Pysr(vetor_entrada, vetor_resultado):
    # Configurações do Pysr ====================================================================== 
    model = PySRRegressor(
        model_selection="best",
        niterations=INF,  # Botei um número bem alto para a condição de parada ser dada apenas pelo tempo
        binary_operators=["+", "*", "-", "/", "^"],
        progress=True,
        # A condição de parada ====
        timeout_in_seconds=10*HORA,
        populations=50,
        population_size=150,
        maxsize=50,
        unary_operators=[
            "sin",
            "cos",
            "exp",
            "log",
            "abs",
            "sinh",
            "cosh",
        ],
        #warm_start=True,
        # Faz com que o pysr rode a partir de um progresso já feito ^
        turbo=True,
        batching=False,
        # Usar se tiver mais de 1000 pontos ^
        nested_constraints={"sin": {"sin": 1, "cos": 1, "sinh": 1, "cosh": 1}, "cos": {"sin": 1, "cos": 1, "sinh": 1, "cosh": 1}, 
                            "sinh": {"sin": 1, "cos": 1, "sinh": 1, "cosh": 1}, "cosh": {"sin": 1, "cos": 1, "sinh": 1, "cosh": 1}, "abs": {"abs": 0}}, 
        constraints={"^": (9, 1)},
        loss="loss(prediction, target) = (prediction - target)^2",
        early_stop_condition="f(loss, complexity) = (loss < 0.00001) && (complexity < 10)",
        equation_file="equacoes.csv",
    )
    model.fit(vetor_entrada, vetor_resultado)
    print(model)

def plota_grafico(xVector, vetor_resultado_real):
    valores_reais = []
    entrada = "equacoes.pkl"
    # Nome que eu defini nas configurações do pysr ^
    model = PySRRegressor.from_file(entrada)
    x0,x1,x2,x3= sp.symbols('x0 x1 x2 x3')

    while True:
        valores_predicao = []
        while True:
            os.system('clear')
            print("+--------------------------------------------------------+")
            print("|                      Programinha                       |")
            print("+--------------------------------------------------------+")
            print("|-> Escolha a equação de predição gerada pelo PySR       |")
            print("|-> Deixe em branco para usar a equação escolhida automa-|")
            print("| ticamente pelo PySR com base na sua seleção de modelo! |")
            print("+--------------------------------------------------------+")
            print("| 0. Voltar                                              |")
            print("+--------------------------------------------------------+\n")

            string_numero_equacao = (input("Selecione a opção e pressione Enter(0 para voltar, 1, ..., quantidade de equações): "))

            if string_numero_equacao == "":
                equacao = PySRRegressor.sympy(model, None)
                break
            
            numero_equacao = int(string_numero_equacao)
            numero_equacao -= 1
            
            if numero_equacao == -1:
                return
            
            elif numero_equacao >= 0:
                equacao = PySRRegressor.sympy(model, numero_equacao)
                break
        # Escolhe qual equação será plotada ^^^ ======================================

        '''
        if len(vetor_resultado_real) == 0:
            arr = np.loadtxt( "dados_treinamento.csv" , delimiter = ',' , dtype = float)
            valores_reais = arr[ : , COLUNA_ARQUIVO_Y ]
                
        else:
            if len(valores_reais) == 0:
                valores_reais = vetor_resultado_real
        '''
        valores_reais = vetor_resultado_real
        
        for i in range(len(xVector)):
            x_atual = xVector[i]
            valores_subs = {x0: x_atual[0], x1: x_atual[1], x2: x_atual[2], x3: x_atual[3]}
            valores_predicao.append(equacao.subs(valores_subs))

        # Ordena os valores em ordem crescente de Delta
        valores_ordenados = sorted(zip(valores_reais, valores_predicao))
        valores_reais_ordenados = [v[0] for v in valores_ordenados]
        valores_predicao_ordenados = [v[1] for v in valores_ordenados]

        # Modifique esta linha para reduzir os arrays pela metade
        #valores_reais_ordenados = valores_reais_ordenados[::]

        # E esta linha também
        #valores_predicao_ordenados = valores_predicao_ordenados[::]

        plt.plot(np.arange(len(valores_reais)), valores_reais_ordenados, color='blue', marker='o', markersize=8, alpha=0.7, linestyle='None', label='Valor Real de G2')
        plt.plot(np.arange(len(valores_predicao)), valores_predicao_ordenados, color='red', marker='x', markersize=14, alpha=0.7, linestyle='None', label='Predição pela eq gerada')

        # Mostro a equação no gráfico
        #plt.text(0.5, 0.95, f'Equação: {equacao}', horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes, fontsize=12)
        
        print(f'eq: {equacao}')
        
        plt.title('Comparação entre Valor Real do Delta e Predição pelo PySR')
        plt.xlabel('Índice dos Pontos')
        plt.ylabel('Valor do G2')

        plt.legend()
        plt.show()
    
    