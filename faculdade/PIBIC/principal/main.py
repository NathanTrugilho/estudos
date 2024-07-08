from funcoes import *

def main():
    x = 0
    y = 0
    while True:
        # Pequena interface =================================================
        os.system('clear')
        print("+---------------------------------------------------------+")
        print("|                  O Regressor simbólico                  |")
        print("+---------------------------------------------------------+")
        print("| 1. Usar a Regressão simbólica                           |")
        print("| 2. Plotar o gráfico para comparar com a predição        |")
        print("| 3. Mostrar resultados                                   |")
        print("| 0. Sair                                                 |")
        print("+---------------------------------------------------------+")
        print("|-> Lembrar de alterar a constante com o arq de entrada!  |")
        print("|-> Lembrar de alterar as colunas de dados de entrada!    |")
        print("+---------------------------------------------------------+\n")

        caso = int(input("-> Selecione a opção (1, 2, 3, 0): "))

        if caso == 0:
            # Encerra o programa
            print("Programa encerrado!\n")
            return 0

        else:                                                                             #usecols é para ele carregar apenas as colunas que quero
            arr = np.loadtxt( "treino.csv" , delimiter = ',' , dtype = float, skiprows=1, usecols=[1,2,3,5,6,7,9]) 
            x = arr[ : ,  [0, 1, 2, 3, 4, 5]] #B, C, D, F, G, H               #skiprows é pra pular a primeira linha (que informa o que é aquele dado)
            y = arr[ : , 6] # J

            '''
            array = np.loadtxt("cofre/dados_teste.csv" , delimiter = ',' , dtype = float)
            w = array[ : ,  [4, 5, 7, 8]]
            z = array[ : , COLUNA_ARQUIVO_Y]
            #'''
            # Será usando quando eu for testar ^

            # Switch case para o usuário escolher o que quer fazer =================================================
            if caso == 1:
                Pysr(x,y)
                pausa_tela()

            elif caso == 2:
                plota_grafico(x,y)
                #plota_grafico(w,z)

            elif caso == 3:
                print(f"\n{PySRRegressor.from_file(ARQUIVO_PKL)}")
                pausa_tela()

            else:
                print("Opção inválida")
                pausa_tela()

main()