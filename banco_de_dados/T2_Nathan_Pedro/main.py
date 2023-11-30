import re #Para verificar nomes com espaço
import PySimpleGUI as psg
from funcoes import *

LEN_CPF = 11
LEN_ESTADO = 2
MAX_LEN_BAIRRO = 40
MIN_LEN_BAIRRO = 3
MAX_LEN_CIDADE = 40
MIN_LEN_CIDADE = 5
MAX_LEN_NOME = 40
MIN_LEN_NOME = 10
MAX_LEN_NOME_LOGIN = 30
MIN_LEN_NOME_LOGIN = 10
MAX_LEN_SENHA = 20
MIN_LEN_SENHA = 8

NOME_LOGIN_GERENTE = 'GerenciaLoja'
SENHA_GERENTE = 'gerente123'

connection = conecta('localhost', 'tecnico', '123456')
if not connection :
    exit()

cursor = connection.cursor()
cursor.execute("use loja;")
janela = janela_login()
#Loop da janela de login (pra escolher se é atendente ou usuário)
while connection:
    eventos, valores = janela.read()
    # Se o usuário clicar em um dos botões ou fechar a janela
    if eventos == psg.WINDOW_CLOSED or eventos == "sair":
        break

    # LOGIN USUARIO ===========================================(Desenvolvimento)==========================================================
    elif eventos == "login_usuario":
        janela.close()
        janela = janela_sistema_usuario()

        while True:
            # Atualizar a janela
            eventos, valores = janela.read()

            # Se o usuário clicar no botão "Fechar"
            if eventos == psg.WINDOW_CLOSED or eventos == "voltar_login_usuario":
                janela.close()
                janela = janela_login()
                break
            elif eventos == "comprar":
                print(valores)
                #print("Você selecionou a Branca !")

                if 'Branca' in  valores[0]:
                    print("Você selecionou a Branca !") 


            # Se o usuário clicar no botão "Login"
            elif eventos == "usuario_logou":
                login_usuario = valores["nome_login_usuario"]
                senha_usuario = valores["senha_usuario"]

                # Verifica se os campos estão preenchidos
                if len(login_usuario) < MIN_LEN_NOME_LOGIN or len(login_usuario) > MAX_LEN_NOME_LOGIN:
                    psg.popup("Login inválido!")
                    continue

                if len(senha_usuario) < MIN_LEN_SENHA or len(senha_usuario) > MAX_LEN_SENHA:
                    psg.popup("Senha inválida!")
                    continue
                
                cursor.execute(f"SELECT nome_login FROM usuario_web WHERE nome_login = '{login_usuario}'")
                if not cursor.fetchone():
                    psg.popup("Este login não está cadastrado!")
                    continue
                
                cursor.execute(f"SELECT senha FROM usuario_web WHERE senha = '{senha_usuario}'")
                if not cursor.fetchone():
                    psg.popup("Senha incorreta!")
                    continue

                
                #fazer a parte principal do código !!!!!!!

    # REGISTRAR USUARIO =============================================(Feito)====================================================
    elif eventos == "registrar_usuario":
        janela.close()
        janela = janela_registrar_usuario()

        while True:
            eventos, valores = janela.read()

            if eventos == psg.WINDOW_CLOSED or eventos == "voltar_registrar_usuario":
                janela.close()
                janela = janela_login()
                break
            
            elif eventos == "registrado":
                nome = valores['nome']
                cpf = valores['cpf']
                bairro = valores['bairro']
                cidade = valores['cidade']
                estado = valores['estado']
                login = valores['login']
                senha = valores['senha']

                if len(nome) < MIN_LEN_NOME or len(nome) > MAX_LEN_NOME or not re.match(r'^[A-Za-z\s]+$', nome):
                    psg.popup("Nome inválido!")
                    continue

                if not len(cpf) == LEN_CPF or not cpf.isdigit():
                    psg.popup("CPF inválido!")
                    continue
                
                if len(bairro) < MIN_LEN_BAIRRO or len(bairro) > MAX_LEN_BAIRRO or not re.match(r'^[A-Za-z\s]+$', bairro):
                    psg.popup("Bairro inválido!")
                    continue

                if len(cidade) < MIN_LEN_CIDADE or len(cidade) > MAX_LEN_CIDADE or not re.match(r'^[A-Za-z\s]+$', cidade):
                    psg.popup("Cidade inválida!")
                    continue

                if (len(estado) != LEN_ESTADO) or not estado.isalpha() or not estado.isupper():
                    psg.popup("Estado inválido!")
                    continue
                
                if len(login) < MIN_LEN_NOME_LOGIN or len(login) > MAX_LEN_NOME_LOGIN:
                    psg.popup("Login inválido!")
                    continue

                if len(senha) < MIN_LEN_SENHA or len(senha) > MAX_LEN_SENHA:
                    psg.popup("Senha inválida!")
                    continue
                
                cursor.execute(f"SELECT cpf FROM usuario WHERE cpf = '{cpf}'")
                if cursor.fetchone():
                    psg.popup("CPF já cadastrado!")
                    continue

                cursor.execute(f"SELECT nome_login FROM usuario_web WHERE nome_login = '{login}'")
                if cursor.fetchone():
                    psg.popup("Este login já está sendo usado!")
                    continue

                cursor.execute(f"INSERT INTO usuario VALUES('{cpf}','{nome}','{bairro}','{cidade}','{estado}')")
                cursor.execute(f"INSERT INTO usuario_web VALUES('{cpf}','{login}','{senha}')")
                connection.commit()

                psg.popup("Conta registrada com sucesso!")
                janela.close()
                janela = janela_login()
                break

    # LOGIN ATENDENTE =====================================================================================================
    elif eventos == "login_atendente":
        janela.close()
        janela = janela_login_atendente()

        while True:
            # Atualizar a janela
            eventos, valores = janela.read()

            if eventos == psg.WINDOW_CLOSED or eventos == "voltar_login_atendente":
                janela.close()
                janela = janela_login()
                break
            
            elif eventos == "atendente_logou":
                login_atendente = valores["nome_login_atendente"]
                senha_atendente = valores["senha_atendente"]

                # Verifica se os campos estão preenchidos
                if len(login_atendente) < MIN_LEN_NOME_LOGIN or len(login_atendente) > MAX_LEN_NOME_LOGIN:
                    psg.popup("Login inválido!")
                    continue

                if len(senha_atendente) < MIN_LEN_SENHA or len(senha_atendente) > MAX_LEN_SENHA:
                    psg.popup("Senha inválida!")
                    continue
                
                cursor.execute(f"SELECT nome_login FROM atendente WHERE nome_login = '{login_atendente}'")
                if not cursor.fetchone():
                    psg.popup("Este login não está cadastrado!")
                    continue
                
                cursor.execute(f"SELECT senha FROM atendente WHERE senha = '{senha_atendente}'")
                if not cursor.fetchone():
                    psg.popup("Senha incorreta!")
                    continue
                
                # SISTEMA ATENDENTE =======================================================================
                janela.close()
                janela = sistema_atendente()

                while True:
                    # Atualizar a janela
                    eventos, valores = janela.read()

                    if eventos == psg.WINDOW_CLOSED or eventos == "voltar_login_atendente":
                        janela.close()
                        janela = janela_login_atendente()
                        break

                    elif eventos == "registrar_usuario_atendente":
                        sub_janela = janela_atendente_registrar_usuario()

                        while True:
                            eventos, valores = sub_janela.read()

                            if eventos == psg.WINDOW_CLOSED or eventos == "voltar_login_atendente":
                                sub_janela.close()
                                break
                            
                            elif eventos == "usuario_atendido_registrado":

                                nome = valores['nome']
                                cpf = valores['cpf']
                                bairro = valores['bairro']
                                cidade = valores['cidade']
                                estado = valores['estado']

                                if len(nome) < MIN_LEN_NOME or len(nome) > MAX_LEN_NOME or not re.match(r'^[A-Za-z\s]+$', nome):
                                    psg.popup("Nome inválido!")
                                    continue

                                if not len(cpf) == LEN_CPF or not cpf.isdigit():
                                    psg.popup("CPF inválido!")
                                    continue
                                
                                if len(bairro) < MIN_LEN_BAIRRO or len(bairro) > MAX_LEN_BAIRRO or not re.match(r'^[A-Za-z\s]+$', bairro):
                                    psg.popup("Bairro inválido!")
                                    continue

                                if len(cidade) < MIN_LEN_CIDADE or len(cidade) > MAX_LEN_CIDADE or not re.match(r'^[A-Za-z\s]+$', cidade):
                                    psg.popup("Cidade inválida!")
                                    continue

                                if (len(estado) != LEN_ESTADO) or not estado.isalpha() or not estado.isupper():
                                    psg.popup("Estado inválido!")
                                    continue
                                                        
                                cursor.execute(f"SELECT cpf FROM usuario WHERE cpf = '{cpf}'")
                                if cursor.fetchone():
                                    psg.popup("CPF já cadastrado!")
                                    continue

                                cursor.execute(f"INSERT INTO usuario VALUES('{cpf}','{nome}','{bairro}','{cidade}','{estado}')")
                                connection.commit()

                                psg.popup("Usuário registrado com sucesso!")
                                sub_janela.close()
                                break

                    elif eventos == "lista_produtos_atendente":
                        cursor.execute("SELECT nome FROM produto")
                        janela["pica"].update(cursor.fetchall())  

    # LOGIN GERENTE =====================================================================================================
    elif eventos == "login_gerente":
        janela.close()
        janela = janela_login_gerente()

        while True:
            # Atualizar a janela
            eventos, valores = janela.read()

            if eventos == psg.WINDOW_CLOSED or eventos == "voltar_login_gerente":
                janela.close()
                janela = janela_login()
                break

            # Se o gerente clicar no botão "Login"
            elif eventos == "gerente_logou":
                login_gerente = valores["nome_login_gerente"]
                senha_gerente = valores["senha_gerente"]

                # Verifica se os campos estão preenchidos
                if len(login_gerente) < MIN_LEN_NOME_LOGIN or len(login_gerente) > MAX_LEN_NOME_LOGIN:
                    psg.popup("Login inválido!")
                    continue

                if len(senha_gerente) < MIN_LEN_SENHA or len(senha_gerente) > MAX_LEN_SENHA:
                    psg.popup("Senha inválida!")
                    continue

                if login_gerente != NOME_LOGIN_GERENTE:
                    psg.popup("Este login não está cadastrado!")
                    continue

                if senha_gerente != SENHA_GERENTE:
                    psg.popup("Senha incorreta!")
                    continue
                
                # SISTEMA DA GERENCIA ======================================================================
                janela.close()
                janela =  sistema_gerencia()
                while True:
                    eventos, valores = janela.read()

                    if eventos == psg.WINDOW_CLOSED or eventos == "voltar_sistema_gerencia":
                        janela.close()
                        janela = janela_login_gerente()
                        break

                    elif eventos == "registrar_atendente":
                        sub_janela = janela_registrar_atendente()

                        while True:
                            eventos, valores = sub_janela.read()

                            if eventos == psg.WINDOW_CLOSED or eventos == "voltar_registrar_atendente":
                                sub_janela.close()
                                break
                            
                            elif eventos == "atendente_registrado":
                                nome_atendente = valores['nome_atendente']
                                cpf_atendente = valores['cpf_atendente']
                                senha_atendente = valores['senha_atendente']

                                if len(nome_atendente) < MIN_LEN_NOME or len(nome_atendente) > MAX_LEN_NOME or not re.match(r'^[A-Za-z\s]+$', nome_atendente):
                                    psg.popup("Nome inválido!")
                                    continue

                                if not len(cpf_atendente) == LEN_CPF or not cpf_atendente.isdigit():
                                    psg.popup("CPF inválido!")
                                    continue

                                if len(senha_atendente) < MIN_LEN_SENHA or len(senha_atendente) > MAX_LEN_SENHA:
                                    psg.popup("Senha inválida!")
                                    continue
                                
                                cursor.execute(f"SELECT cpf FROM atendente WHERE cpf = '{cpf_atendente}'")
                                if cursor.fetchone():
                                    psg.popup("CPF já cadastrado!")
                                    continue

                                cursor.execute(f"INSERT INTO atendente VALUES('{cpf_atendente}','{nome_atendente}','{senha_atendente}')")
                                connection.commit()

                                psg.popup("Atendente registrado com sucesso!")
                                sub_janela.close()
                                break

cursor.close()
connection.close()
janela.close()