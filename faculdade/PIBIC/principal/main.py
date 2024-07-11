from funcoes import *

def main():
    while True:
        # Pequena interface =================================================
        os.system('clear')
        print("+---------------------------------------------------------+")
        print("|                  O Regressor simbólico                  |")
        print("+---------------------------------------------------------+")
        print("| 1. Usar a Regressão simbólica                           |")
        print("| 2. Plotar o gráfico para comparar com a predição        |")
        print("| 3. Observar métricas de erro -> MSE, RMSE, MAE ...      |")
        print("| 4. Mostrar resultados                                   |")
        print("| 0. Sair                                                 |")
        print("+---------------------------------------------------------+")
        print("|-> Lembrar de alterar a constante com o arq de entrada!  |")
        print("|-> Lembrar de alterar as colunas de dados de entrada!    |")
        print("+---------------------------------------------------------+\n")

        caso = int(input("-> Selecione a opção (1, 2, 3, 4, 0): "))

        if caso == 0:
            # Encerra o programa
            print("Programa encerrado!\n")
            return 0

        else:                                                                             
            # Switch case para o usuário escolher o que quer fazer =================================================
            if caso == 1:                                                                     
                Pysr()
                pausa_tela()

            elif caso == 2:                                                                  
                plota_grafico()

            elif caso == 3:                                                                      
                observa_metricas()

            elif caso == 4:
                print(f"\n{PySRRegressor.from_file(EQUACOES_PKL)}")
                pausa_tela()
            
            else:
                print("Opção inválida")
                pausa_tela()

main()