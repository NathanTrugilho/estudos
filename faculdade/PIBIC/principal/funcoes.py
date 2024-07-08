import os
from pysr import PySRRegressor
import matplotlib.pyplot as plt 
import numpy as np

ARQUIVO_PKL = "equacoes.pkl"
HORA = 3600
INF = 100000000000

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
        #timeout_in_seconds=10*HORA,
        populations=100,
        population_size=100,
        maxsize=30,
        unary_operators=[
            "sin",
            "cos",
            "exp",
            "log",
            "sinh",
            "cosh",
            "erf",
        ],
        warm_start=True,
        # Faz com que o pysr rode a partir de um progresso já feito ^
        turbo=True,
        batching=False,
        # Usar se tiver mais de 1000 pontos ^
        nested_constraints={"sin": {"sin": 1, "cos": 1, "sinh": 1, "cosh": 1}, "cos": {"sin": 1, "cos": 1, "sinh": 1, "cosh": 1},
                            "sinh": {"sin": 1, "cos": 1, "sinh": 1, "cosh": 1}, "cosh": {"sin": 1, "cos": 1, "sinh": 1, "cosh": 1}},
        constraints={"^": (9, 1)},
        loss="loss(prediction, target) = (prediction - target)^2", # MSE (erro quadrático médio)
        early_stop_condition="f(loss, complexity) = (loss < 0.000001) && (complexity < 10)",
        equation_file="equacoes.csv",
    )
    model.fit(vetor_entrada, vetor_resultado)
    print(model)

def plota_grafico(xVector, vetor_resultado_real):
    # Inicializo os vetores
    valores_reais = []
    valores_predicao = []

    # Defino o nome do arquivo e carrego ele para a variável "model"
    entrada = ARQUIVO_PKL
    model = PySRRegressor.from_file(entrada)

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

            # Escolhe qual equação será plotada
            if string_numero_equacao == "":
                valores_predicao = model.predict(xVector)
                equacao = PySRRegressor.sympy(model)
                break
            
            numero_equacao = int(string_numero_equacao)
            numero_equacao -= 1
            
            if numero_equacao == -1:
                return
            
            elif numero_equacao >= 0:
                valores_predicao = model.predict(xVector, numero_equacao)
                equacao = PySRRegressor.sympy(model, numero_equacao)
                break

        # Carrega os valores reais para serem comparados com os valores de predição
        valores_reais = vetor_resultado_real
        
        # Ordena os valores em ordem crescente
        valores_ordenados = sorted(zip(valores_reais, valores_predicao))
        valores_reais_ordenados = [v[0] for v in valores_ordenados]
        valores_predicao_ordenados = [v[1] for v in valores_ordenados]

        plt.plot(np.arange(len(valores_reais)), valores_reais_ordenados, color='blue', marker='o', markersize=8, alpha=1, linestyle='None', label='Valor real do MDO (m³/h)')
        plt.plot(np.arange(len(valores_predicao)), valores_predicao_ordenados, color='red', marker='o', markersize=7, alpha=1, linestyle='None', label='Predição pela eq gerada')
      
        plt.title('Comparação entre Valor do MDO(m³/h) e Predição pelo PySR')
        plt.xlabel('Índice dos Pontos')
        plt.ylabel('MDO')

        plt.legend()
        print(f'\nEquação escolhida simplificada: {equacao}')
        plt.show()
    