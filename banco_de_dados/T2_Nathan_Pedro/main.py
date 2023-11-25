import PySimpleGUI as sg
import mysql.connector
from funcoes import janela_login, janela_login_usuario, janela_login_atendente

# Definir as credenciais do usuário
host = "localhost"
user = "tecnico"
password = "123456"

# Conectar ao MySQL
connection = mysql.connector.connect(host=host, user=user, password=password)

# Verificar se o banco de dados já existe
cursor = connection.cursor()
cursor.execute("SELECT COUNT(*) FROM information_schema.SCHEMATA WHERE schema_name = 'loja'")

# Se o banco de dados não existir, criá-lo
if cursor.fetchone()[0] == 0:
    cursor.execute("CREATE DATABASE loja")

# Fechar a conexão

cursor.close()
connection.close()

janela = janela_login()

#Loop da janela de login (pra escolher se é atendente ou usuário)
while True:
    eventos, valores = janela.read()

    # Se o usuário clicar em um dos botões ou fechar a janela
    if eventos == sg.WINDOW_CLOSED:
        break
    elif eventos == "usuario":
        # Loop principal
        janela = janela_login_usuario()
        while True:
            # Atualizar a janela
            eventos, valores = janela.read()

            # Se o usuário clicar no botão "Login"
            if eventos == "Login":
                # Verifique se os campos estão preenchidos
                if valores["Nome"] == "" or valores["Senha"] == "":
                    sg.popup("Preencha todos os campos!")
                else:
                    # Faça algo com as credenciais do usuário
                    print(f"Nome: {valores['Nome']}")
                    print(f"Senha: {valores['Senha']}")

            # Se o usuário clicar no botão "Fechar"
            if eventos == sg.WINDOW_CLOSED:
                break
        
    elif eventos == "atendente":
        print("blabla")
        # Faça algo relacionado ao login do atendente aqui

janela.close()


