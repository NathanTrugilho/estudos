import PySimpleGUI as sg
import mysql.connector
from funcoes import janela_login, janela_login_usuario, janela_login_atendente, janela_registrar_usuario, verifica_bd

connection = verifica_bd()
cursor = connection.cursor()
janela = janela_login()

#Loop da janela de login (pra escolher se é atendente ou usuário)
while True:
    eventos, valores = janela.read()
    # Se o usuário clicar em um dos botões ou fechar a janela
    if eventos == sg.WINDOW_CLOSED or eventos == "sair":
        break

    elif eventos == "login_usuario":
        janela.close()
        janela = janela_login_usuario()

        while True:
            # Atualizar a janela
            eventos, valores = janela.read()

            # Se o usuário clicar no botão "Fechar"
            if eventos == sg.WINDOW_CLOSED or eventos == "voltar":
                janela.close()
                janela = janela_login()
                break

            # Se o usuário clicar no botão "Login"
            elif eventos == "usuario_logou":
                nome_usuario = valores["nome"]
                senha_usuario = valores["senha"]

                # Verifique se os campos estão preenchidos
                if nome_usuario == "" or senha_usuario == "":
                    sg.popup("Preencha todos os campos!")
                else:
                    cursor.execute("SELECT nome_login, senha FROM usuario_web WHERE nome_login = %s AND senha = %s;", (nome_usuario, senha_usuario))
                    # Verifica se o usuario existe na tabela (lembrar de fazer o resto dps)
                    if cursor.fetchone():
                        sg.popup("Deu bom!")
                    else:
                        sg.popup("Deu merda!")


    elif eventos == "registrar_usuario":
        janela.close()
        janela = janela_registrar_usuario()

        while True:
            eventos, valores = janela.read()
            if eventos == sg.WINDOW_CLOSED or eventos == "voltar":
                janela.close()
                janela = janela_login()
                break

    elif eventos == "login_atendente":
        janela.close()
        janela = janela_login_atendente()

        while True:
            # Atualizar a janela
            eventos, valores = janela.read()

            # Se o usuário clicar no botão "Login"
            if eventos == "login_ate":
                # Verifique se os campos estão preenchidos
                if valores["Nome"] == '' or valores["Senha"] == '':
                    sg.popup("Preencha todos os campos!")
                else:
                    # Faça algo com as credenciais do usuário
                    print(f"Nome: {valores['Nome']}")
                    print(f"Senha: {valores['Senha']}")

            # Se o usuário clicar no botão voltar
            if eventos == "voltar":
                janela.close()
                janela = janela_login()
                break
            # Se o usuário clicar no botão "Fechar"
            if eventos == sg.WINDOW_CLOSED:
                janela.close()
                break
        
cursor.close()
connection.close()
janela.close()