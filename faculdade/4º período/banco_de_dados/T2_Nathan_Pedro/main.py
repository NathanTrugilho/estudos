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
                cursor.execute(f"SELECT senha FROM usuario_web WHERE nome_login = '{login_usuario}'")
                hash_armazenado = cursor.fetchone()
                hash_armazenado = hash_armazenado[0]
                #12345678910
                print(hash_armazenado)
                print(senha_usuario)
                #senha_usuario = criar_hash_senha(senha_usuario)
                print(senha_usuario)
                #hash_armazenado = senha_usuario

                #verificar_senha1(senha_usuario,hash_armazenado)
                #cursor.execute(f"SELECT senha FROM usuario_web WHERE senha = '{senha_usuario}'")
                #if not cursor.fetchone():
                if not verificar_senha(senha_usuario,hash_armazenado):
                    psg.popup("Senha incorreta!")
                    continue

                qtd_produto = 0
                qtd_produtos = {}
                id_conta = 0
                id_item = 0
                id_produto = 0 
                valor = 0
                nome = ''
                #Pega o CPF============================
                cursor.execute("SELECT cpf_usuario FROM usuario_web where nome_login = %s",(login_usuario,))
                id_conta = cursor.fetchall()
                id_conta = id_conta[0][0]
                #Pega o id conta====================================================================================
                cursor.execute("SELECT id FROM conta where cpf_usuario = %s",(id_conta,))
                id_conta = cursor.fetchall()
                id_conta= id_conta[0][0]
                #Cria um carrinho====================================================================================
                cursor.execute("INSERT INTO carrinho_de_compras (id_conta) VALUES (%s)",(id_conta,))
                connection.commit()
                cursor.execute("SELECT id,nome,id_produto from item")
                itens = cursor.fetchall()
                cursor.execute("SELECT id,valor from produto")
                produtos = cursor.fetchall()
                cursor.execute("SELECT MAX(id) AS maior_id FROM carrinho_de_compras")
                id_carrinho = cursor.fetchall()
                id_carrinho = list(map(lambda x: x[0],id_carrinho))
                id_carrinho = id_carrinho[0]
                janela.close()
                janela = janela_sistema_usuario()
                #====================================================================================
                while True:
                    # Atualizar a janela
                    #print("Os itens são : ",itens)
                    # Se o usuário clicar no botão "Fechar"
                    eventos, valores = janela.read()
                    if eventos == psg.WINDOW_CLOSED or eventos == "voltar_login_usuario":
                        janela.close()
                        janela = janela_login_usuario()
                        cursor.execute("DELETE FROM relacao_carrinho_item WHERE id_carrinho_de_compras = %s", (id_carrinho,))
                        connection.commit()
                        break
                    #==============================================Lidando com compras===============================================
                    elif eventos == "comprar":
                        #Para debugar ele está printando tudo que recebe da janela
                        #Eu percorro minha lista de valores em busca de um produto selecionado ou seja que seja diferente de [] 
                        #Depois eu pego o id com base no meu banco de dados de id que eu fiz a culsulta lá em cima
                        #Depois eu pego a quantidade , já sabendo que a quantidade sempre vem depois do produto
                        #Lembre que valores[chave] é um tipo lista , logo mesmo com um valor vc precisa colocar esse [0]
                        #Se a chave for um inteiro é porquê o valor é o tipo do produto
                        for chave in valores:
                            if valores[chave] and isinstance(chave, int) :
                                for id_item1,tipo,id_produtofor in itens:
                                    if  valores[chave][0] in tipo:
                                        id_item = id_item1
                                        id_produto = id_produtofor
                                        for id_produto2 , valor_produto in produtos:
                                            if id_produto2 == id_produto:
                                                valor = int(valor_produto)
                                                break   
                                        nome = tipo
                                        break
                            elif valores[chave] and id_item:
                                qtd_produto = valores[chave]
                                id_conta = int(id_conta)
                                id_item = int(id_item)
                                #=============================
                                qtd_produto = qtd_produto
                                cursor.execute("select id_item from relacao_carrinho_item where id_carrinho_de_compras = %s",(id_carrinho,))
                                item_carrinho = cursor.fetchall()
                                item_carrinho = list(map(lambda x: x[0],item_carrinho))
                                print(item_carrinho)
                                if id_item not in item_carrinho:
                                    qtd_produtos[id_item] = int(qtd_produto)
                                    valor = valor*int(qtd_produto)
                                    cursor.execute("select quantidade from item where id = %s",(id_item,))
                                    quantidade_item = cursor.fetchall()
                                    qtd_item = list(map(lambda x: x[0],quantidade_item))
                                    if qtd_item[0] >= int(qtd_produto):
                                        cursor.execute("INSERT INTO relacao_carrinho_item VALUES(%s,%s,%s,%s,%s,%s)", (id_carrinho,id_conta, id_item, qtd_produto,valor,nome))
                                        connection.commit()
                                    else:
                                        psg.popup(f"Se alcame rapaz , não temos isso tudo! Nossa quantidade em estoque é : {qtd_item[0]}")
                                else:
                                    qtd_produtos[id_item] += int(qtd_produto)
                                    valor = valor*int(qtd_produtos[id_item])
                                    cursor.execute("select quantidade from item where id = %s",(id_item,))
                                    quantidade_item = cursor.fetchall()
                                    qtd_item = list(map(lambda x: x[0],quantidade_item))
                                    if qtd_item[0] >= int(qtd_produto):
                                        cursor.execute("UPDATE relacao_carrinho_item SET quantidade = quantidade + %s ,valor = %s WHERE id_item = %s", (qtd_produto,valor, id_item))
                                        connection.commit()
                                    else:
                                         psg.popup(f"Se alcame rapaz , não temos isso tudo! Nossa quantidade em estoque é : {qtd_item[0]}")
                                id_item = 0
                                

                    #==============================================Lidando com compras===============================================
                    elif eventos == "ver_carrinho":
                        cursor.execute("select nome,quantidade,valor from relacao_carrinho_item where id_carrinho_de_compras = %s",(id_carrinho,))
                        compras = cursor.fetchall()
                        janela.close()
                        cursor.execute("SELECT SUM(valor) AS total_valor FROM relacao_carrinho_item WHERE id_carrinho_de_compras = %s",(id_carrinho,))
                        total_carrinho = cursor.fetchone()
                        total_carrinho = total_carrinho[0]
                        janela = janela_carrinho(compras,total_carrinho)
                        while True:
                            eventos, valores = janela.read()
                            # Se o usuário clicar no botão "Fechar"
                            if eventos == psg.WINDOW_CLOSED or eventos == "voltar_sistema_usuario_carrinho": 
                                janela.close()
                                janela =janela_sistema_usuario()
                                break
                            if eventos == "novo_carrinho":
                                janela.close()
                                janela =janela_sistema_usuario()
                                cursor.execute("DELETE FROM relacao_carrinho_item WHERE id_carrinho_de_compras = %s", (id_carrinho,))
                                cursor.execute("INSERT INTO carrinho_de_compras (id_conta) VALUES (%s)",(id_conta,))
                                cursor.execute("SELECT MAX(id) AS maior_id FROM carrinho_de_compras")
                                id_carrinho = cursor.fetchall()
                                id_carrinho = list(map(lambda x: x[0],id_carrinho))
                                id_carrinho = id_carrinho[0]
                                qtd_produto = 0
                                qtd_produtos = {}
                                valor = 0
                                nome = 0
                                id_item = 0
                                break
                            if eventos == "comprar_carrinho":
                                cursor.execute(f"INSERT INTO pedido (status, data, id_conta, cpf_atendente) VALUES('confirmado', curdate(), {id_conta},'NULL')")
                                connection.commit()
                                cursor.execute(f"SELECT id FROM pedido ORDER BY id DESC LIMIT 1")
                                id_pedido = cursor.fetchone()
                                id_pedido = id_pedido[0]
                                sub_janela = pagamento(total_carrinho)
                                forma_de_pagamento = ''

                                # SERVE PARA TIRAR DO ESTOQUE E ADICIONAR OS VALORES NA TABELA "relacao_pedido_item" (aquela da relação N por N). As alterações só serão salvas depois do usuário comprar
                                for p in qtd_produtos:
                                    cursor.execute(f"UPDATE item SET quantidade = (quantidade - {qtd_produtos[p]}) WHERE id = {p}") #muda estoque
                                    
                                    if qtd_produtos[p] > 0:
                                        cursor.execute(f"INSERT INTO relacao_item_pedido VALUES ({id_pedido}, {p}, {qtd_produtos[p]}) ") #adiciona na relacao n por n
                                # PARTE QUE VERIFICA O PAGAMENTO 
                                while True:
                                    event, values = sub_janela.read()

                                    if event == psg.WIN_CLOSED or event == 'Cancelar pagamento':
                                        for p in qtd_produtos:
                                           cursor.execute(f"UPDATE item SET quantidade = (quantidade + {qtd_produtos[p]}) WHERE id = {p}")
                                        psg.popup("Pagamento cancelado!")
                                        sub_janela.close()
                                        janela.close()
                                        cursor.execute(f"UPDATE pedido SET status = 'cancelado' WHERE id = {id_pedido}")
                                        sai = 0
                                        break

                                    elif event in ('Pix', 'Débito', 'Crédito', 'Boleto'):
                                        sub_janela['forma_pagamento'].update(f"{event}")
                                        forma_de_pagamento = event

                                    elif event == 'Pagar':
                                        parcelas = values['parcela']
                                        parcelas_int = int(parcelas)

                                        if parcelas_int < 1:
                                            psg.popup("Quantidade de parcelas inválida!")
                                            continue
                                        
                                        if forma_de_pagamento == '':
                                            psg.popup("Selecione uma forma de pagamento")
                                            continue

                                        if parcelas_int > 24:
                                            psg.popup("O número máximo de parcelas é de 24 vezes!")
                                            continue

                                        valor_parcela = (total_carrinho/parcelas_int)
                                        psg.popup(f"Pagamento realizado no {forma_de_pagamento} em {parcelas} vez(es) de {valor_parcela} reais.")

                                        cursor.execute(f"INSERT INTO pagamento(id_pedido, parcela, forma_pagamento, valor) VALUES ({id_pedido}, 1, '{forma_de_pagamento}', {valor_parcela})")
                                        cursor.execute(f"UPDATE pedido SET status = 'pago' WHERE id = {id_pedido}")
                                        connection.commit()
                                        sub_janela.close()
                                        cursor.execute("INSERT INTO carrinho_de_compras (id_conta) VALUES (%s)",(id_conta,))
                                        connection.commit()
                                        cursor.execute("SELECT MAX(id) AS maior_id FROM carrinho_de_compras")
                                        id_carrinho = cursor.fetchall()
                                        id_carrinho = list(map(lambda x: x[0],id_carrinho))
                                        id_carrinho = id_carrinho[0]
                                        break

                                janela.close()
                                janela = janela_sistema_usuario()
                                break

                    #fazer a parte principal do código !!!!!!!
    # REGISTRAR USUARIO =============================================(Feito)====================================================
    elif eventos == "registrar_usuario":
        janela.close()
        janela = janela_registrar_usuario()

        while True:
            eventos, valores = janela.read()
            
            # VERIFICA SE O USUÁRIO VOLTOU
            if eventos == psg.WINDOW_CLOSED or eventos == "voltar_registrar_usuario":
                janela.close()
                janela = janela_login()
                break
            
            # FAZ AS VERIFICAÇÕES PARA INSERIR DADOS VÁLIDOS =====================================================================
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
                
                # INSERE OS DADOS DO NOVO USUÁRIO NO BANCO DE DADOS ======================================================
                print(senha)
                senha = criar_hash_senha(senha)
                print(senha)
                cursor.execute(f"INSERT INTO usuario VALUES('{cpf}','{nome}','{bairro}','{cidade}','{estado}')")
                #cursor.execute(f"INSERT INTO usuario_web VALUES('{cpf}','{login}','{senha}')")
                cursor.execute("INSERT INTO usuario_web VALUES (%s ,%s ,%s)",(cpf,login,senha))
                cursor.execute(f"INSERT INTO conta(cpf_usuario) VALUES('{cpf}')")
                connection.commit()

                psg.popup("Conta registrada com sucesso!")
                janela.close()
                janela = janela_login()
                break

    # LOGIN ATENDENTE ======================================(FEITO)===============================================================
    elif eventos == "login_atendente":
        janela.close()
        janela = janela_login_atendente()

        while True:
            # Atualizar a janela =====
            eventos, valores = janela.read()

            # Verifica se o usuário fechou =========
            if eventos == psg.WINDOW_CLOSED or eventos == "voltar_login_atendente":
                janela.close()
                janela = janela_login()
                break
            
            elif eventos == "atendente_logou":
                login_atendente = valores["nome_login_atendente"]
                senha_atendente = valores["senha_atendente"]

                # VERIFICA SE OS CAMPOS ESTÃO PREENCHIDOS  =================
                if len(login_atendente) < MIN_LEN_NOME_LOGIN or len(login_atendente) > MAX_LEN_NOME_LOGIN:
                    psg.popup("Login inválido!")
                    continue

                if len(senha_atendente) < MIN_LEN_SENHA or len(senha_atendente) > MAX_LEN_SENHA:
                    psg.popup("Senha inválida!")
                    continue
                # ==========================================================

                # VERIFICA AS CREDENCIAIS DO USUARIO ============
                cursor.execute(f"SELECT nome_login FROM atendente WHERE nome_login = '{login_atendente}'")
                if not cursor.fetchone():
                    psg.popup("Este login não está cadastrado!")
                    continue

                cursor.execute(f"SELECT senha FROM atendente WHERE nome_login = '{login_atendente}'")
                hash_armazenado = cursor.fetchone()
                hash_armazenado = hash_armazenado[0]

                if not verificar_senha(senha_atendente,hash_armazenado):
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
                    
                    # REGISTRA UM NOVO USUÁRIO QUE ESTÁ COMPRANDO POR LIGAÇÃO TELEFÔNICA ================================================
                    elif eventos == "registrar_usuario_atendente":
                        sub_janela = janela_atendente_registrar_usuario()

                        while sai:
                            eventos, valores = sub_janela.read()

                            # VERIFICA SE O USUARIO VOLTOU =================================================================================
                            if eventos == psg.WINDOW_CLOSED or eventos == "voltar_login_atendente":
                                sub_janela.close()
                                break
                            
                            elif eventos == "usuario_atendido_registrado":

                                nome = valores['nome']
                                cpf = valores['cpf']
                                bairro = valores['bairro']
                                cidade = valores['cidade']
                                estado = valores['estado']

                                # VERIFICA SE OS DADOS SÃO VÁLIDOS ========================================================================
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
                                # ===========================================================================================================
                               
                                # INSERE O NOVO USUARIO NA TABELA 
                                cursor.execute(f"INSERT INTO usuario VALUES('{cpf}','{nome}','{bairro}','{cidade}','{estado}')")
                                cursor.execute(f"INSERT INTO conta(cpf_usuario) VALUES('{cpf}')")
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
                        
                        if resultado == None:
                            psg.popup("Cliente não cadastrado!")
                            continue

                        psg.popup("CPF inserido!")
                        id_conta = resultado[0]

                        cursor.execute(f"INSERT INTO carrinho_de_compras(id_conta) VALUES ('{id_conta}')")
                        connection.commit()
                        cursor.execute("SELECT id FROM carrinho_de_compras ORDER BY id DESC LIMIT 1;") # Pega o id do último carrinho criado !!! (que é o atual)
                        resultado = cursor.fetchone()
                        id_carrinho = resultado[0]

                        while sai:
                            eventos, valores = janela.read()
                            
                            # VERIFICA SE O USUÁRIO VOLTOU E APAGA O CARRINHO SE FOR VERDADE ==================
                            if eventos == psg.WINDOW_CLOSED or eventos == "voltar_login_atendente":
                                janela.close()
                                sai = 0
                                cursor.execute(f"DELETE FROM carrinho_de_compras WHERE id = {id_carrinho}")
                                connection.commit()
                                break
                            
                            elif eventos == "insere_cpf":
                                cursor.execute(f"DELETE FROM carrinho_de_compras WHERE id = {id_carrinho}")
                                
                                # PEGA OS DADOS ============================================= 
                                cpf = valores['cpf']
                                if not len(cpf) == LEN_CPF or not cpf.isdigit():
                                            psg.popup("CPF inválido!")
                                            continue
                                
                                cursor.execute(f"SELECT id FROM conta WHERE cpf_usuario = '{cpf}'")
                                resultado = cursor.fetchone()
                                if resultado == None:
                                    psg.popup("Cliente não cadastrado!")
                                    continue
                                
                                # INSERE O NOVO CPF ===========================================
                                psg.popup("CPF inserido!")
                                id_conta = resultado[0]
                                cursor.execute(f"INSERT INTO carrinho_de_compras(id_conta) VALUES ('{id_conta}')")
                                connection.commit()
                                cursor.execute("SELECT id FROM carrinho_de_compras ORDER BY id DESC LIMIT 1;") # Pega o id do último carrinho criado !!! (que é o atual)
                                resultado = cursor.fetchone()
                                id_carrinho = resultado[0]
                            
                            #ADICIONA O ITEM NO CARRINHO =======================================================
                            elif eventos == "adic_carrinho":
                                produtos = ['camiseta', 'camisa', 'casaco', 'cropped', 'calça', 'bermuda', 'saia', 'tênis', 'sapato', 'sapatilha']
                                nome_item = ['','','','','','','','','','']
                                quantidade_int = [0,0,0,0,0,0,0,0,0,0]
                                valor_produto = [0,0,0,0,0,0,0,0,0,0]
                                id_item = [0,0,0,0,0,0,0,0,0,0]
                                verifica_quantidade = 10
                                total_carrinho = 0
                                quantidade = 0 
                                permissao = 1

                                for i in range (10):
                                    quantidade = valores[f'qtd_{produtos[i]}']
                                    quantidade_int[i] = int(quantidade)

                                    if quantidade_int[i] > 0:
                                        nome_item[i] = valores[f'lista_{produtos[i]}'][0]
                                        cursor.execute(f"SELECT id FROM item WHERE nome = '{produtos[i]} {nome_item[i]}'")
                                        resultado = cursor.fetchone()
                                        id_item[i] = resultado[0]

                                        cursor.execute(f"SELECT quantidade FROM item WHERE id = {id_item[i]}")
                                        resultado = cursor.fetchone()
                                        quantidade_estoque = resultado[0]

                                    if (quantidade_estoque - quantidade_int[i]) < 0:
                                        psg.popup(f"Se acalme, rapaz! só temos {quantidade_estoque} unidades de {produtos[i]} {nome_item[i]}.")
                                        permissao = 0
                                        break 
                                
                                if permissao == 0:
                                    continue

                                for i in range (10):
                                    
                                    if quantidade_int[i] > 0:
                                        cursor.execute(f"SELECT valor FROM produto JOIN item ON produto.id = item.id_produto WHERE produto.nome = '{produtos[i]}' LIMIT 1;")
                                        resultado = cursor.fetchone()
                                        valor_produto[i] = resultado[0] * quantidade_int[i]
                                        total_carrinho += valor_produto[i]

                                        cursor.execute(f"INSERT INTO relacao_carrinho_item VALUES({id_carrinho},{id_conta},{id_item[i]},{quantidade_int[i]},{valor_produto[i]},'{produtos[i]} {nome_item[i]}')")
                                        verifica_quantidade -= 1

                                if verifica_quantidade == 10:
                                    psg.popup("Selecione pelo menos um item com alguma quantidade válida para prosseguir")
                                    continue
                                
                                psg.popup("Itens adicionados ao carrinho !")

                                # CRIA O PEDIDO =======================================================
                                cursor.execute(f"INSERT INTO pedido (status, data, id_conta, cpf_atendente) VALUES('confirmado', curdate(), {id_conta}, {cpf_atendente})")
                                connection.commit()

                                # CRIA A JANELA DE PAGAMENTO E PEGA OS DADOS NECESSÁRIOS PARA CRIAR UM PAGAMENTO =====================================
                                cursor.execute(f"SELECT id FROM pedido ORDER BY id DESC LIMIT 1")
                                resultado = cursor.fetchone()
                                id_pedido = resultado[0]
                                sub_janela = pagamento(total_carrinho)
                                forma_de_pagamento = ''

                                # SERVE PARA TIRAR DO ESTOQUE E ADICIONAR OS VALORES NA TABELA "relacao_pedido_item" (aquela da relação N por N). As alterações só serão salvas depois do usuário comprar
                                for i in range (10):
                                    if quantidade_int[i] > 0:

                                        cursor.execute(f"UPDATE item SET quantidade = (quantidade - {quantidade_int[i]}) WHERE id = {id_item[i]}") #muda estoque
                                        cursor.execute(f"INSERT INTO relacao_item_pedido VALUES ({id_pedido}, {id_item[i]}, {quantidade_int[i]}) ") #adiciona na relacao n por n

                                # PARTE QUE VERIFICA O PAGAMENTO (AS PARCELAS, O MÉTODO DE PAGAMENTO OU SE O USUÁRIO DECIDIU CANCELAR A COMPRA) ===========
                                while True:
                                    event, values = sub_janela.read()
                                    
                                    # CANCELA A COMPRA E MUDA O STATUS DO PEDIDO PARA CANCELADO ============
                                    if event == psg.WIN_CLOSED or event == 'Cancelar pagamento':
                                        psg.popup("Pagamento cancelado!")
                                        sub_janela.close()
                                        janela.close()
                                        janela = sistema_atendente()
                                        cursor.execute(f"UPDATE pedido SET status = 'cancelado' WHERE id = {id_pedido}")
                                        sai = 0
                                        break
                                    
                                    # VERIFICA O MÉTODO DE PAGAMENTO
                                    elif event in ('Pix', 'Débito', 'Crédito', 'Boleto'):
                                        sub_janela['forma_pagamento'].update(f"{event}")
                                        forma_de_pagamento = event

                                    # VERIFICA SE A QUANTIDADE DE PARCELAS É VÁLIDA 
                                    elif event == 'Pagar':
                                        parcelas = values['parcela']
                                        parcelas_int = int(parcelas)

                                        if parcelas_int < 1:
                                            psg.popup("Quantidade de parcelas inválida!")
                                            continue
                                        
                                        if forma_de_pagamento == '':
                                            psg.popup("Selecione uma forma de pagamento")
                                            continue

                                        if parcelas_int > 24:
                                            psg.popup("O número máximo de parcelas é de 24 vezes!")
                                            continue

                                        # INSERE O PAGAMENTO NA TABELA E ALTERA O STATUS DO PEDIDO PARA "PAGO"
                                        valor_parcela = (total_carrinho/parcelas_int)
                                        psg.popup(f"Pagamento realizado no {forma_de_pagamento} em {parcelas} vez(es) de {valor_parcela} reais.")
                                        cursor.execute(f"INSERT INTO pagamento(id_pedido, parcela, forma_pagamento, valor) VALUES ({id_pedido}, 1, '{forma_de_pagamento}', {valor_parcela})")
                                        cursor.execute(f"UPDATE pedido SET status = 'pago' WHERE id = {id_pedido}")
                                        connection.commit()
                                        sub_janela.close()
                                        janela.close()
                                        janela = sistema_atendente()
                                        sai = 0
                                        break
                    
                    # VERIFICAÇÃO BOBINHA 
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
                                print(senha_atendente)
                                senha_atendente = criar_hash_senha(senha_atendente)
                                print(senha_atendente)
                                cursor.execute("INSERT INTO atendente VALUES(%s , %s , %s)",(cpf_atendente,nome_atendente,senha_atendente))
                                connection.commit()

                                psg.popup("Atendente registrado com sucesso!")
                                sub_janela.close()
                                break
                    elif eventos == "excluir_atendente":
                        sub_janela = janela_excluir_atendente()
                        while True:
                            eventos, valores = sub_janela.read()

                            if eventos == psg.WINDOW_CLOSED or eventos == "voltar_excluir_atendente":
                                sub_janela.close()
                                break
                            if eventos == "excluir_atendente":
                                cpf_atendente = valores['cpf_atendente']
                                if not len(cpf_atendente) == LEN_CPF or not cpf_atendente.isdigit():
                                    psg.popup("CPF inválido!")
                                    continue
                                cursor.execute(f"DELETE FROM atendente WHERE cpf ={cpf_atendente}")
                                connection.commit()
                                psg.popup("Atendente Apagado com sucesso!")
                                sub_janela.close()
                                break



                    elif eventos == "todos_pedidos_conta":
                        sub_janela = sub_janela_total_pedido_conta_id()
                        while True:
                            eventos, valores = sub_janela.read()
                            
                            if eventos == psg.WINDOW_CLOSED or eventos == "voltar_sistema_gerente":
                                sub_janela.close()
                                break

                            elif eventos == "enviar":
                                sub_janela.close()
                                id_conta = valores["id_conta"]
                                id_conta = int(id_conta)
                                print(id_conta)
                                #cursor.execute(f"SELECT count(*) FROM pedido WHERE id_conta = {id_conta} GROUP BY id_conta")
                                cursor.execute(f"SELECT id, status, data, cpf_atendente FROM pedido WHERE id_conta = {id_conta}")
                                total_pedidos = cursor.fetchall()
                                print(total_pedidos)
                                #total_pedidos = total_pedidos[0][0]
                                print(total_pedidos)
                                sub_janela = sub_janela_total_pedido_conta(total_pedidos)
                                while True:
                                    eventos, valores = sub_janela.read()
                                    if eventos == psg.WINDOW_CLOSED or eventos == "voltar_sistema_gerente":
                                        sub_janela.close()
                                        break
                    elif eventos == "maior_cliente":
                        cursor.execute("""
                                SELECT c.cpf_usuario,sum(pg.valor) 
                                FROM conta c
                                JOIN pedido p ON c.id = p.id_conta
                                JOIN pagamento pg ON p.id = pg.id_pedido
                                GROUP BY c.cpf_usuario
                                ORDER BY SUM(pg.valor) DESC
                                LIMIT 1
                            """)
                        maior_cliente = cursor.fetchall()
                        print(type(maior_cliente[0][0]))
                        cursor.execute(f"""SELECT nome FROM usuario WHERE cpf = {maior_cliente[0][0]}""")
                        nome_maior_cliente = cursor.fetchone()
                        print(nome_maior_cliente)
                        nome_maior_cliente = str(nome_maior_cliente[0])
                        print(nome_maior_cliente)
                        sub_janela = sub_janela_maior_cliente(nome_maior_cliente,maior_cliente[0][1])
                        while True:
                            eventos, valores = sub_janela.read()
                            if eventos == psg.WINDOW_CLOSED or eventos == "voltar_sistema_gerente":
                                sub_janela.close()
                                break

                    elif eventos == "todos_produtos_carrinho":
                        sub_janela =  sub_todos_produtos_carrinho_id()
                        while True:
                            eventos, valores = sub_janela.read()
                            
                            if eventos == psg.WINDOW_CLOSED or eventos == "voltar_sistema_gerente":
                                sub_janela.close()
                                break

                            elif eventos == "enviar":
                                sub_janela.close()
                                id_carrinho= valores["id_carrinho"]
                                id_carrinho = int(id_carrinho)
                                print(id_carrinho)
                                #cursor.execute(f"SELECT count(*) FROM pedido WHERE id_conta = {id_conta} GROUP BY id_conta")
                                cursor.execute(f"SELECT id_conta_carrinho_de_compras, id_item, valor, nome FROM relacao_carrinho_item WHERE id_carrinho_de_compras = {id_carrinho}")
                                total_produtos = cursor.fetchall()
                                print(total_produtos)
                                #total_pedidos = total_pedidos[0][0]
                                print(total_produtos)
                                sub_janela = sub_todos_produtos_carrinho(total_produtos)
                                while True:
                                    eventos, valores = sub_janela.read()
                                    if eventos == psg.WINDOW_CLOSED or eventos == "voltar_sistema_gerente":
                                        sub_janela.close()
                                        break
                    elif eventos == "media_anual":
                        cursor.execute("SELECT YEAR(pedido.data) AS ano, AVG(pagamento.valor) AS media_vendas_anual FROM pagamento JOIN pedido ON pagamento.id_pedido = pedido.id GROUP BY YEAR(pedido.data)")
                        media_anual = cursor.fetchall()
                        print(media_anual)
                        sub_janela = sub_janela_media_anual(media_anual)

                        while True:
                            eventos, valores = sub_janela.read()

                            if eventos == psg.WINDOW_CLOSED or eventos == "voltar_sistema_gerente":
                                sub_janela.close()
                                break
                    elif eventos == "dados_usuarios_cadastrados":
                        cursor.execute("SELECT count(cpf_usuario) FROM usuario_web")
                        resultado = cursor.fetchone()
                        quantidade_usuarios_web = resultado[0]

                        cursor.execute("SELECT count(cpf) FROM usuario")
                        resultado = cursor.fetchone()
                        quantidade_usuarios_atendidos = resultado[0] - quantidade_usuarios_web
                        sub_janela = sub_janela_dados_usuarios(quantidade_usuarios_web, quantidade_usuarios_atendidos)
    
                        while True:
                            eventos, valores = sub_janela.read()

                            cursor.execute("SELECT * FROM usuario")
                            resultados = cursor.fetchall()

                            for tupla in resultados:
                                print(tupla)

                            if eventos == psg.WINDOW_CLOSED or eventos == "voltar_sistema_gerente":
                                sub_janela.close()
                                break
                        
                    elif eventos == "media_anual":
                        cursor.execute("SELECT YEAR(pedido.data) AS ano, AVG(pagamento.valor) AS media_vendas_anual FROM pagamento JOIN pedido ON pagamento.id_pedido = pedido.id GROUP BY YEAR(pedido.data)")
                        media_anual = cursor.fetchall()
                        print(media_anual)
                        sub_janela = sub_janela_media_anual(media_anual)

                        while True:
                            eventos, valores = sub_janela.read()

                            if eventos == psg.WINDOW_CLOSED or eventos == "voltar_sistema_gerente":
                                sub_janela.close()
                                break

                    elif eventos == "formas_pagamento":
                        cursor.execute("SELECT forma_pagamento, count(forma_pagamento) AS qtd, sum(valor) AS valor FROM pagamento GROUP BY forma_pagamento ORDER BY qtd DESC")
                        resultado = cursor.fetchall()
                        forma_pagamento = [0,0,0,0]
                        quantidade_pagamento = [0,0,0,0]
                        valor_pagamento = [0,0,0,0]

                        for i in range(4):
                            forma_pagamento[i] = resultado[i][0]
                            quantidade_pagamento[i] = resultado[i][1]
                            valor_pagamento[i] = resultado[i][2]

                        sub_janela = sub_janela_pagamento_mais_utilizado(forma_pagamento, quantidade_pagamento, valor_pagamento)
                        while True:
                            eventos, valores = sub_janela.read()

                            if eventos == psg.WINDOW_CLOSED or eventos == "voltar_sistema_gerente":
                                sub_janela.close()
                                break
                    
                    elif eventos == "maior_numero_vendas":
                        cursor.execute("select year(data), count(pagamento.id) as qtd from pedido join pagamento on pagamento.id_pedido = pedido.id group by year(data) order by qtd desc limit 1")
                        resultado = cursor.fetchone()
                        maior_num_ano = resultado[0]

                        cursor.execute("select month(data), count(pagamento.id) as qtd from pedido join pagamento on pagamento.id_pedido = pedido.id group by month(data) order by qtd desc limit 1")
                        resultado = cursor.fetchone()
                        maior_num_mes = resultado[0]

                        sub_janela = sub_janela_maior_numero_vendas(maior_num_ano, maior_num_mes)
                        while True:
                            eventos, valores = sub_janela.read()

                            if eventos == psg.WINDOW_CLOSED or eventos == "voltar_sistema_gerente":
                                sub_janela.close()
                                break

                    elif eventos == "compras_todos_meses":

                        sub_janela = sub_janela_compras_todos_meses()
                        
                        while True:
                            eventos, valores = sub_janela.read()

                            if eventos == psg.WINDOW_CLOSED or eventos == "voltar_sistema_gerente":
                                sub_janela.close()
                                break
                            
                            elif eventos == "busca_compra":
                                sub_janela["output"].update('')
                                verifica_ano = valores['ano']
                                
                                if not verifica_ano.isdigit():
                                    psg.popup("Insira um ano válido!")
                                    continue
                                
                                verifica_ano = int(verifica_ano)

                                cursor.execute(f"select cpf_usuario from pedido join conta on pedido.id_conta = conta.id where year(data) = '{verifica_ano}' and status = 'pago' group by id_conta having count(distinct month(data)) = 12;")
                                resultado = cursor.fetchone()

                                if not resultado == None:
                                    resultado = resultado[0]
                                    print(resultado)
                                    continue
                                
                                print("Nenhum usuário fez compras em todos os meses deste ano!")

                    elif eventos == "melhor_atendente":
                        
                        cursor.execute("select cpf_atendente, count(cpf_atendente) as qtd from pedido group by cpf_atendente order by qtd desc limit 1")
                        resultado = cursor.fetchone()
                        cpf_atendente = resultado[0]
                        quantidade_vendas = resultado[1]

                        sub_janela = sub_janela_melhor_atendente(cpf_atendente, quantidade_vendas)
                        
                        while True:
                            eventos, valores = sub_janela.read()

                            if eventos == psg.WINDOW_CLOSED or eventos == "voltar_sistema_gerente":
                                sub_janela.close()
                                break
                    
                    elif eventos == "filtrar_usuarios":
                        sub_janela = sub_janela_filtrar_usuarios()

                        while True:
                            eventos, valores = sub_janela.read()

                            if eventos == psg.WINDOW_CLOSED or eventos == "voltar_sistema_gerente":
                                sub_janela.close()
                                break
                            
                            elif eventos == "pesquisar":
                                sub_janela["output"].update('')
                                bairro = valores['bairro']
                                cidade = valores['cidade']
                                estado = valores['estado']
                                
                                # VERIFICA SE OS DADOS SÃO VÁLIDOS ========================================================================                                
                                if len(bairro) < MIN_LEN_BAIRRO or len(bairro) > MAX_LEN_BAIRRO or not re.match(r'^[A-Za-z\s]+$', bairro):
                                    if len(bairro) != 0:
                                        psg.popup("Bairro inválido!")
                                        continue

                                if len(cidade) < MIN_LEN_CIDADE or len(cidade) > MAX_LEN_CIDADE or not re.match(r'^[A-Za-z\s]+$', cidade):
                                    if len(cidade) != 0:
                                        psg.popup("Cidade inválida!")
                                        continue

                                if (len(estado) != LEN_ESTADO) or not estado.isalpha() or not estado.isupper():
                                    if len(estado) != 0:
                                        psg.popup("Estado inválido!")
                                        continue
                                
                                cursor.execute(f"select cpf from usuario where estado = '{estado}' and cidade = '{cidade}' and bairro = '{bairro}'")
                                resultados = cursor.fetchall()

                                for resultado in resultados:
                                    print(resultado[0])

cursor.close()
connection.close()
janela.close()