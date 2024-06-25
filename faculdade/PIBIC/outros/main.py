from itertools import product
from funcoes import *

def main():
    x = 0
    y = 0
    while True:
        # Pequena interface =================================================
        os.system('clear')
        print("+--------------------------------------------------------+")
        print("|                      Programinha                       |")
        print("+--------------------------------------------------------+")
        print("| 1. Usar a Regressão simbólica                          |")
        print("| 2. Plotar o gráfico para comparar com a predição       |")
        print("| 3. Sair                                                |")
        print("+--------------------------------------------------------+")
        print("|-> Primeiro Calcular os valores de delta antes de usar a|")
        print("| regressão simbólica ou plotar o gráfico !!!            |")
        print("+--------------------------------------------------------+\n")

        caso = int(input("Selecione a opção (1, 2, 3): "))

        if caso == 3:
            # Encerra o programa
            print("Programa encerrado!\n")
            return 0

        else:
            # Fazer para os quatro (g1, g2 ...)
            arr = np.loadtxt( "dados_treinamento.csv" , delimiter = ',' , dtype = float)
            x = arr[ : ,  [4, 5, 7, 8]]
            y = arr[ : , COLUNA_ARQUIVO_Y]

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
                
            else:
                print("Opção inválida")
                pausa_tela()

main()