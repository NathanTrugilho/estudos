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
        janela = janela_login_usuario()
        while True:
            eventos, valores = janela.read()
                # Se o usuário clicar no botão "Login"
            if eventos == psg.WINDOW_CLOSED or eventos == "voltar_login_usuario":
                janela.close()
                janela = janela_login()
                break
            elif eventos == "usuario_logou":
                login_usuario = valores["nome_login_usuario"]
                senha_usuario = valores["senha_usuario"]
                print("Entrei aqui !")
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

                janela.close()
                janela = janela_sistema_usuario()
                qtd_produto = 0
                id_conta = 1
                id_item = 0
                id_produto = 0 
                valor = 0
                nome = ''
                cursor.execute("INSERT INTO carrinho_de_compras (id_conta) VALUES (%s)",(id_conta,))
                while True:
                    # Atualizar a janela
                    eventos, valores = janela.read()
                    botoes_compras = ["comprar1","comprar2","comprar3","comprar4","comprar5","comprar6","comprar7","comprar8","comprar9","comprar10"]
                    cursor.execute("select id,nome,id_produto from item")
                    itens = cursor.fetchall()
                    cursor.execute("select id,valor from produto")
                    produtos = cursor.fetchall()
                    cursor.execute("SELECT MAX(id) AS maior_id FROM carrinho_de_compras")
                    id_carrinho = cursor.fetchall()
                    id_carrinho = list(map(lambda x: x[0],id_carrinho))
                    id_carrinho = id_carrinho[0]
                    print("O id do carrinho é : ",id_carrinho)
                    #print("Os itens são : ",itens)
                    # Se o usuário clicar no botão "Fechar"
                    if eventos == psg.WINDOW_CLOSED or eventos == "voltar_login_usuario":
                        janela.close()
                        janela = janela_login_usuario()
                        break
                    #==============================================Lidando com compras===============================================
                    #Não tem como colocar todos os botões com o mesmo nome pois ai os outros não estavam ativando , logo cada botão deve ter seu nome
                    elif eventos in botoes_compras:
                        #Para debugar ele está printando tudo que recebe da janela
                        print(valores)
                        #Eu percorro minha lista de valores em busca de um produto selecionado ou seja que seja diferente de [] 
                        #Depois eu pego o id com base no meu banco de dados de id que eu fiz a culsulta lá em cima
                        #Depois eu pego a quantidade , já sabendo que a quantidade sempre vem depois do produto
                        #Lembre que valores[chave] é um tipo lista , logo mesmo com um valor vc precisa colocar esse [0]
                        #Verificar se é necessário deixar o usuario aumentar a quantidade depois
                        for chave in valores:
                            if valores[chave] and isinstance(chave, int) :
                                print(valores[chave][0])
                                print(type(chave))
                                print(type(valores[chave]))
                                for id,tipo,id_produto in itens:
                                    if  valores[chave][0] in tipo:
                                        id_item = id
                                        id_produto = id_produto
                                        print(tipo)
                                        print(id_item)
                                        for id , valor_produto in produtos:
                                            if id == id_produto:
                                                valor == valor_produto   
                                        nome = tipo
                                        break
                            elif valores[chave] and id_item:
                                qtd_produto = valores[chave]
                                print(qtd_produto)
                                id_conta = int(id_conta)
                                id_item = int(id_item)
                                qtd_produto = qtd_produto[0]
                                cursor.execute("select id_item from relacao_carrinho_item")
                                produto_carrinho = cursor.fetchall()
                                print(produto_carrinho)
                                produto_carrinho = list(map(lambda x: x[0],produto_carrinho))
                                print(produto_carrinho)
                                if id_item not in produto_carrinho:
                                    cursor.execute("INSERT INTO relacao_carrinho_item VALUES(%s,%s,%s,%s,%s,%s)", (id_carrinho,id_conta, id_item, qtd_produto[0],valor,nome))
                                    cursor.fetchall()
                                else:
                                    cursor.execute("UPDATE relacao_carrinho_item SET quantidade = quantidade + %s WHERE id_item = %s", (qtd_produto[0], id_item))
                                    cursor.fetchall()
                                id_item = 0
                                connection.commit()
                                break
                                
                    #==============================================Lidando com compras===============================================
                    elif eventos == "ver_carrinho":
                        cursor.execute("select nome,quantidade from relacao_carrinho_item")
                        compras = cursor.fetchall()
                        janela.close()
                        janela = janela_carrinho(compras)
                        while True:
                            eventos, valores = janela.read()
                            # Se o usuário clicar no botão "Fechar"
                            if eventos == psg.WINDOW_CLOSED or eventos == "voltar_sistema_usuario": 
                                janela.close()
                                janela =janela_sistema_usuario()
                                break
                            if eventos == "comprar_carrinho":
                                connection.commit()
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
                
                cursor.execute(f"SELECT cpf FROM atendente WHERE nome_login = '{login_atendente}'")
                resultado = cursor.fetchone()
                cpf_atendente = resultado[0]

                # SISTEMA ATENDENTE =======================================================================
                janela.close()
                janela = sistema_atendente()

                while True:
                    # Atualizar a janela
                    eventos, valores = janela.read()
                    sai = 1
                    if eventos == psg.WINDOW_CLOSED or eventos == "voltar_login_atendente":
                        janela.close()
                        janela = janela_login_atendente()
                        break

                    elif eventos == "registrar_usuario_atendente":
                        sub_janela = janela_atendente_registrar_usuario()

                        while sai:
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

                    elif eventos == "insere_cpf":
                        
                        #PEGA OS DADOS =============================================
                        cpf = valores['cpf']
                        if not len(cpf) == LEN_CPF or not cpf.isdigit():
                                    psg.popup("CPF inválido!")
                                    continue
                        
                        cursor.execute(f"SELECT id FROM conta WHERE cpf_usuario = '{cpf}'")
                        resultado = cursor.fetchone()
                        id_conta = resultado[0]
                        cursor.execute(f"INSERT INTO carrinho_de_compras(id_conta) VALUES ('{id_conta}')")
                        
                        cursor.execute("SELECT id FROM carrinho_de_compras ORDER BY id DESC LIMIT 1;") #Pega o último carrinho criado
                        resultado = cursor.fetchone()
                        id_carrinho = resultado[0]

                        while sai:
                            eventos, valores = janela.read()

                            if eventos == psg.WINDOW_CLOSED or eventos == "voltar_login_atendente":
                                janela.close()
                                sai = 0
                                break
                            
                            #ADICIONA O ITEM NO CARRINHO =======================================================
                            elif eventos == "adic_carrinho":
                                verifica_quantidade = 10
                                total_carrinho = 0
                                quantidade = 0 

                                quantidade = valores['qtd_camiseta']
                                quantidade_int = int(quantidade)
                                print(quantidade_int)
                                if quantidade_int > 0:
                                    nome_item = valores['lista_camiseta'][0]
                                    cursor.execute(f"SELECT id FROM item WHERE nome = 'camiseta {nome_item}'")
                                    resultado = cursor.fetchone()
                                    id_item = resultado[0]
                                    cursor.execute(f"SELECT valor FROM produto JOIN item ON produto.id = item.id_produto WHERE produto.nome = 'camiseta' LIMIT 1;")
                                    resultado = cursor.fetchone()
                                    valor_produto = resultado[0] * quantidade_int
                                    total_carrinho += valor_produto

                                    cursor.execute(f"INSERT INTO relacao_carrinho_item VALUES({id_carrinho},{id_conta},{id_item},{quantidade},{valor_produto},'camiseta {nome_item}')")
                                    verifica_quantidade -= 1

                                quantidade = valores['qtd_camisa']
                                quantidade_int = int(quantidade) 
                                if quantidade_int > 0:

                                    nome_item = valores['lista_camisa'][0]
                                    cursor.execute(f"SELECT id FROM item WHERE nome = 'camisa {nome_item}'")
                                    resultado = cursor.fetchone()
                                    id_item = resultado[0]
                                    cursor.execute(f"SELECT valor FROM produto JOIN item ON produto.id = item.id_produto WHERE produto.nome = 'camisa' LIMIT 1;")
                                    resultado = cursor.fetchone()
                                    valor_produto = resultado[0] * quantidade_int
                                    total_carrinho += valor_produto 
                                    
                                    cursor.execute(f"INSERT INTO relacao_carrinho_item VALUES({id_carrinho},{id_conta},{id_item},{quantidade},{valor_produto},'camisa {nome_item}')")
                                    verifica_quantidade -= 1

                                quantidade = valores['qtd_casaco']
                                quantidade_int = int(quantidade) 
                                if quantidade_int > 0:

                                    nome_item = valores['lista_casaco'][0]
                                    cursor.execute(f"SELECT id FROM item WHERE nome = 'casaco {nome_item}'")
                                    resultado = cursor.fetchone()
                                    id_item = resultado[0]
                                    cursor.execute(f"SELECT valor FROM produto JOIN item ON produto.id = item.id_produto WHERE produto.nome = 'casaco' LIMIT 1;")
                                    resultado = cursor.fetchone()
                                    valor_produto = resultado[0] * quantidade_int
                                    total_carrinho += valor_produto 
                                    
                                    cursor.execute(f"INSERT INTO relacao_carrinho_item VALUES({id_carrinho},{id_conta},{id_item},{quantidade},{valor_produto},'casaco {nome_item}')")
                                    verifica_quantidade -= 1

                                quantidade = valores['qtd_cropped']
                                quantidade_int = int(quantidade) 
                                if quantidade_int > 0:

                                    nome_item = valores['lista_cropped'][0]
                                    cursor.execute(f"SELECT id FROM item WHERE nome = 'cropped {nome_item}'")
                                    resultado = cursor.fetchone()
                                    id_item = resultado[0]
                                    cursor.execute(f"SELECT valor FROM produto JOIN item ON produto.id = item.id_produto WHERE produto.nome = 'cropped' LIMIT 1;")
                                    resultado = cursor.fetchone()
                                    valor_produto = resultado[0] * quantidade_int
                                    total_carrinho += valor_produto 
                                    
                                    cursor.execute(f"INSERT INTO relacao_carrinho_item VALUES({id_carrinho},{id_conta},{id_item},{quantidade},{valor_produto},'cropped {nome_item}')")
                                    verifica_quantidade -= 1

                                quantidade = valores['qtd_calça']
                                quantidade_int = int(quantidade) 
                                if quantidade_int > 0:

                                    nome_item = valores['lista_calça'][0]
                                    cursor.execute(f"SELECT id FROM item WHERE nome = 'calça {nome_item}'")
                                    resultado = cursor.fetchone()
                                    id_item = resultado[0]
                                    cursor.execute(f"SELECT valor FROM produto JOIN item ON produto.id = item.id_produto WHERE produto.nome = 'calça' LIMIT 1;")
                                    resultado = cursor.fetchone()
                                    valor_produto = resultado[0] * quantidade_int
                                    total_carrinho += valor_produto 
                                    
                                    cursor.execute(f"INSERT INTO relacao_carrinho_item VALUES({id_carrinho},{id_conta},{id_item},{quantidade},{valor_produto},'calça {nome_item}')")
                                    verifica_quantidade -= 1

                                quantidade = valores['qtd_bermuda']
                                quantidade_int = int(quantidade) 
                                if quantidade_int > 0:

                                    nome_item = valores['lista_bermuda'][0]
                                    cursor.execute(f"SELECT id FROM item WHERE nome = 'bermuda {nome_item}'")
                                    resultado = cursor.fetchone()
                                    id_item = resultado[0]
                                    cursor.execute(f"SELECT valor FROM produto JOIN item ON produto.id = item.id_produto WHERE produto.nome = 'bermuda' LIMIT 1;")
                                    resultado = cursor.fetchone()
                                    valor_produto = resultado[0] * quantidade_int
                                    total_carrinho += valor_produto

                                    cursor.execute(f"INSERT INTO relacao_carrinho_item VALUES({id_carrinho},{id_conta},{id_item},{quantidade},{valor_produto},'bermuda {nome_item}')")
                                    verifica_quantidade -= 1

                                quantidade = valores['qtd_saia']
                                quantidade_int = int(quantidade) 
                                if quantidade_int > 0:

                                    nome_item = valores['lista_saia'][0]
                                    cursor.execute(f"SELECT id FROM item WHERE nome = 'saia {nome_item}'")
                                    resultado = cursor.fetchone()
                                    id_item = resultado[0]
                                    cursor.execute(f"SELECT valor FROM produto JOIN item ON produto.id = item.id_produto WHERE produto.nome = 'saia' LIMIT 1;")
                                    resultado = cursor.fetchone()
                                    valor_produto = resultado[0] * quantidade_int
                                    total_carrinho += valor_produto 
                                    
                                    cursor.execute(f"INSERT INTO relacao_carrinho_item VALUES({id_carrinho},{id_conta},{id_item},{quantidade},{valor_produto},'saia {nome_item}')")
                                    verifica_quantidade -= 1

                                quantidade = valores['qtd_tênis']
                                quantidade_int = int(quantidade) 
                                if quantidade_int > 0:

                                    nome_item = valores['lista_tênis'][0]
                                    cursor.execute(f"SELECT id FROM item WHERE nome = 'tênis {nome_item}'")
                                    resultado = cursor.fetchone()
                                    id_item = resultado[0]
                                    cursor.execute(f"SELECT valor FROM produto JOIN item ON produto.id = item.id_produto WHERE produto.nome = 'tênis' LIMIT 1;")
                                    resultado = cursor.fetchone()
                                    valor_produto = resultado[0] * quantidade_int
                                    total_carrinho += valor_produto 
                                    
                                    cursor.execute(f"INSERT INTO relacao_carrinho_item VALUES({id_carrinho},{id_conta},{id_item},{quantidade},{valor_produto},'tênis {nome_item}')")
                                    verifica_quantidade -= 1

                                quantidade = valores['qtd_sapato']
                                quantidade_int = int(quantidade) 
                                if quantidade_int > 0:

                                    nome_item = valores['lista_sapato'][0]
                                    cursor.execute(f"SELECT id FROM item WHERE nome = 'sapato {nome_item}'")
                                    resultado = cursor.fetchone()
                                    id_item = resultado[0]
                                    cursor.execute(f"SELECT valor FROM produto JOIN item ON produto.id = item.id_produto WHERE produto.nome = 'sapato' LIMIT 1;")
                                    resultado = cursor.fetchone()
                                    valor_produto = resultado[0] * quantidade_int
                                    total_carrinho += valor_produto 
                                    
                                    cursor.execute(f"INSERT INTO relacao_carrinho_item VALUES({id_carrinho},{id_conta},{id_item},{quantidade},{valor_produto},'sapato {nome_item}')")
                                    verifica_quantidade -= 1

                                quantidade = valores['qtd_sapatilha']
                                quantidade_int = int(quantidade) 
                                if quantidade_int > 0:

                                    nome_item = valores['lista_sapatilha'][0]
                                    cursor.execute(f"SELECT id FROM item WHERE nome = 'sapatilha {nome_item}'")
                                    resultado = cursor.fetchone()
                                    id_item = resultado[0]
                                    cursor.execute(f"SELECT valor FROM produto JOIN item ON produto.id = item.id_produto WHERE produto.nome = 'sapatilha' LIMIT 1;")
                                    resultado = cursor.fetchone()
                                    valor_produto = resultado[0] * quantidade_int
                                    total_carrinho += valor_produto 
                                    
                                    cursor.execute(f"INSERT INTO relacao_carrinho_item VALUES({id_carrinho},{id_conta},{id_item},{quantidade},{valor_produto},'sapatilha {nome_item}')")
                                    verifica_quantidade -= 1
                                
                                if verifica_quantidade == 10:
                                    psg.popup("Selecione pelo menos um item com alguma quantidade válida para prosseguir")
                                    continue

                                psg.popup("Itens adicionados ao carrinho !")
                                cursor.execute(f"INSERT INTO pedido (status, data, id_conta, cpf_atendente) VALUES('confirmado', curdate(), {id_conta}, {cpf_atendente})")
                                connection.commit()

                                cursor.execute(f"SELECT id FROM pedido ORDER BY id DESC LIMIT 1")
                                resultado = cursor.fetchone()
                                id_pedido = resultado[0]

                                pagamento(total_carrinho, id_pedido)

                    elif eventos == "adic_carrinho":
                        psg.popup("Insira o CPF do usuário antes de adicionar no carrinho")

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