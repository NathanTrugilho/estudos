import PySimpleGUI as psg
import mysql.connector
import bcrypt

# Função para criar um hash de senha
def criar_hash_senha(senha):
    # Crie o hash usando a senha e o salt gerado internamente pelo bcrypt
    hash_senha = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())

    # Retorne o hash
    return hash_senha
def verificar_senha(senha, hash_armazenado):
    # Verifique se a senha corresponde ao hash armazenado
    return bcrypt.checkpw(senha.encode('utf-8'), hash_armazenado.encode('utf-8'))
def verificar_senha1(senha, hash_armazenado):
    # Verifique se a senha corresponde ao hash armazenado
    return bcrypt.checkpw(senha, hash_armazenado)
def janela_login():
    psg.theme('Reddit')
    layout_login = [
        [psg.Text("Meu Banco de Dados", size=(20, 1), font=('Arial', 25), justification='center', pad=((0, 0), (30, 20)))],
        [psg.Button("Login como Usuário", size=(30, 2), button_color=("white", "#2196F3"), key="login_usuario", pad=((0, 0), (10, 5)))],
        [psg.Text("Registrar conta", size=(12, 1), text_color='#000080', enable_events=True, key="registrar_usuario", justification='center', pad=((0, 0),(0, 15)))],
        [psg.Button("Login como Atendente", size=(30, 2), button_color=("white", "#4CAF50"), key="login_atendente", pad=((0, 0), (10, 10)))],
        [psg.Button("Login como Gerente", size=(30, 2), button_color=("white", "#FF5252"), key="login_gerente", pad=((0, 0), (10, 10)))],
        [psg.Button("Sair", size=(12, 1), button_color=("white", "#333333"), key="sair", pad=((0, 0), (20, 15)))]
    ]
    return psg.Window("Login", layout_login, background_color="white", element_justification='c')

def janela_sistema_usuario():
    psg.theme('Reddit')
    layout_sistema_usuario = [
        [psg.Text("Página de Compras",text_color='black', size=(20, 1), font=('Arial', 25), justification='center', pad=((0, 0), (20, 30))),
        psg.Button("Ver carrinho", size=(10, 4), button_color=("White", "Green"), key="ver_carrinho", pad=((0, 0), (10,10)))],
        [psg.Text("Camisa preço: 40R$",text_color='black', size=(20, 1), font=('Arial', 20), justification='center', pad=((0, 0), (20, 30))),
        psg.Listbox(["camisa social preta","camisa social branca","camisa regata branca","camisa regata estampada","camisa polo preta"],size=(20,4),select_mode=psg.LISTBOX_SELECT_MODE_SINGLE),psg.Text("Quantidade:"), psg.Input(size=(10,1), key= "qtd_camisa"),
        psg.Text("Camiseta preço : 30 R$",text_color='black', size=(20, 1), font=('Arial', 20), justification='center', pad=((0, 0), (20, 30))),
        psg.Listbox(["camiseta vermelha","camiseta verde","camiseta preta","camiseta azul","camiseta branca"],size=(20,4),select_mode=psg.LISTBOX_SELECT_MODE_SINGLE), psg.Text("Quantidade:"), psg.Input(size=(10,1), key= "qtd_camiseta")],
        
        [psg.Text("Casaco preço : 75 R$",text_color='black', size=(20, 1), font=('Arial', 20), justification='center', pad=((0, 0), (20, 30))),
        psg.Listbox(["casaco vermelho","casaco branco","casaco preto","casaco verde"],size=(20,4),select_mode=psg.LISTBOX_SELECT_MODE_SINGLE), psg.Text("Quantidade:"), psg.Input(size=(10,1), key= "qtd_casaco"),
        psg.Text("Cropped preço : 15 R$",text_color='black', size=(20, 1), font=('Arial', 20), justification='center', pad=((0, 0), (20, 30))),
        psg.Listbox(["cropped vermelho","cropped preto","cropped branco","cropped verde"],size=(20,4),select_mode=psg.LISTBOX_SELECT_MODE_SINGLE), psg.Text("Quantidade:"), psg.Input(size=(10,1), key= "qtd_cropped")],
        
        [psg.Text("Calça preço : 60 R$",text_color='black', size=(20, 1), font=('Arial', 20), justification='center', pad=((0, 0), (20, 30))),
        psg.Listbox(["calça vermelha","calça preta","calça branca","calça verde"],size=(20,4),select_mode=psg.LISTBOX_SELECT_MODE_SINGLE), psg.Text("Quantidade:"), psg.Input(size=(10,1), key= "qtd_calça"),
       
        psg.Text("Bermuda preço : 50 R$",text_color='black', size=(20, 1), font=('Arial', 20), justification='center', pad=((0, 0), (20, 30))),
        psg.Listbox(["bermuda vermelha","bermuda preta","bermuda branca","bermuda verde"],size=(20,4),select_mode=psg.LISTBOX_SELECT_MODE_SINGLE), psg.Text("Quantidade:"), psg.Input(size=(10,1), key= "qtd_bermuda")],
        
        [psg.Text("Saia preço : 120 R$",text_color='black', size=(20, 1), font=('Arial', 20), justification='center', pad=((0, 0), (20, 30))),
        psg.Listbox(["saia vermelha","saia preta","saia branca","saia verde"],size=(20,4),select_mode=psg.LISTBOX_SELECT_MODE_SINGLE), psg.Text("Quantidade:"), psg.Input(size=(10,1), key= "qtd_saia"),
        
        psg.Text("Tênis preço : 300 R$",text_color='black', size=(20, 1), font=('Arial', 20), justification='center', pad=((0, 0), (20, 30))),
        psg.Listbox(["tênis vermelho","tênis preto","tênis branco","tênis verde"],size=(20,4),select_mode=psg.LISTBOX_SELECT_MODE_SINGLE), psg.Text("Quantidade:"), psg.Input(size=(10,1), key= "qtd_tênis")],
        
        [psg.Text("Sapato preço : 380 R$",text_color='black', size=(20, 1), font=('Arial', 20), justification='center', pad=((0, 0), (20, 30))),
        psg.Listbox(["sapato vermelho","sapato preta","sapato branca","sapato verde"],size=(20,4),select_mode=psg.LISTBOX_SELECT_MODE_SINGLE), psg.Text("Quantidade:"), psg.Input(size=(10,1), key= "qtd_sapato"),
       
        psg.Text("Sapatilha preço : 200 R$",text_color='black', size=(20, 1), font=('Arial', 20), justification='center', pad=((0, 0), (20, 30))),
        psg.Listbox(["sapatilha vermelha","sapatilha preta","sapatilha branca","sapatilha verde"],size=(20,4),select_mode=psg.LISTBOX_SELECT_MODE_SINGLE), psg.Text("Quantidade:"), psg.Input(size=(10,1), key= "qtd_sapatilha")],

        [psg.Button("Comprar", size=(12, 1), button_color=("white", "green"), key="comprar", pad=((0, 0), (20, 15)))],

        [psg.Button("Voltar", size=(12, 1), button_color=("white", "#000080"), key="voltar_login_usuario", pad=((0, 0), (20, 15)))]

    ]
    return psg.Window("Login de usuário", layout_sistema_usuario, background_color="white", element_justification='c')


def janela_carrinho(compras,total):
    psg.theme('Reddit')
    layout_carrinho = [
        [psg.Text("Carrinho",text_color='black', size=(20, 1), font=('Arial', 25), justification='center', pad=((0, 0), (20, 30)))],
    ]

    for nome,qtd,valor in compras: 
        layout_carrinho.extend([  # Use extend para adicionar elementos à lista principal
            [psg.Text(nome,size=(30, 1), justification='right'),psg.Text(qtd,size=(6, 1), justification='center'),psg.Text(valor,size=(6, 1), justification='center')],
        ])
    layout_carrinho.extend([ 

        [psg.Text("Total : " ,justification='center',pad=((0,0),(10,20))),psg.Text(total,justification='center',pad=((0,0),(10,20)))],
        [psg.Button("Comprar", size=(12, 1), button_color=("white", "green"), key="comprar_carrinho", pad=((0, 0), (20, 15)))],
        [psg.Button("Apagar esse carrinho", size=(12, 1), button_color=("white", "red"), key="novo_carrinho", pad=((0, 0), (20, 15)))],
        [psg.Button("Voltar", size=(12, 1), button_color=("white", "#000080"), key="voltar_sistema_usuario_carrinho", pad=((0, 0), (20, 15)))],
    ]
    )
    return psg.Window("Login de usuário", layout_carrinho, background_color="white", element_justification='c')



def janela_login_usuario():
    psg.theme('Reddit')
    layout_login_usuario = [
        [psg.Text("Login de usuário",text_color='black', size=(20, 1), font=('Arial', 25), justification='center', pad=((0, 0), (20, 30)))],
        [psg.Text("Login:", size=(6, 1), justification='right'), psg.Input(size=(30, 10), justification="center", key= "nome_login_usuario",default_text="joao@email.com")],
        [psg.Text("Senha:", size=(6, 1), justification='right'), psg.Input(size=(30,10), justification="center", key= "senha_usuario", password_char='*',default_text="senha123")],
        [psg.Button("Logar", size=(20, 2), button_color=("white", "#2E8B57"), key="usuario_logou", pad=((0, 0), (20, 10)))],
        [psg.Button("Voltar", size=(12, 1), button_color=("white", "#000080"), key="voltar_login_usuario", pad=((0, 0), (20, 15)))],
    ]
    return psg.Window("Login de usuário", layout_login_usuario, background_color="white", element_justification='c')

def janela_registrar_usuario():
    psg.theme('Reddit')
    layout_registrar_usuario = [
        [psg.Text('Cadastro de Novo Usuário', font=('Arial', 25), justification='center', pad=((0,0), (20,30)))],
        [psg.Text('Nome:', justification='right', size=(10,1)), psg.InputText(key='nome'), psg.Text('(10-40 chars)')],
        [psg.Text('CPF:', justification='right', size=(10,1)), psg.InputText(key='cpf'), psg.Text('    (11 chars)')],
        [psg.Text('Bairro:', justification='right', size=(10,1)), psg.InputText(key='bairro'), psg.Text(' (3-40 chars)')],
        [psg.Text('Cidade:', justification='right', size=(10,1)), psg.InputText(key='cidade'), psg.Text(' (5-40 chars)')],
        [psg.Text('Estado:', justification='right', size=(10,1)), psg.InputText(key='estado'), psg.Text('      Sigla     ')],
        [psg.Text('Login:', justification='right', size=(10,1)), psg.InputText(key='login'), psg.Text('(10-30 chars)')],
        [psg.Text('Senha:', justification='right', size=(10,1)), psg.InputText(key='senha', password_char='*'), psg.Text(' (8-20 chars)')],
        [psg.Button("Voltar", key='voltar_registrar_usuario', button_color=("white", "#000080"), size=(8, 2), pad=((0, 140), (25, 25))), psg.Button('Registrar', size=(20, 2), button_color=("white", "#2E8B57"), key="registrado")]
    ]
    return psg.Window("Registrar usuario", layout_registrar_usuario, element_justification='c')

def janela_login_atendente():
    psg.theme('Reddit')
    layout_login_atendente = [
        [psg.Text("Login de atendente",text_color='black', size=(20, 1), font=('Arial', 25), justification='center', pad=((0, 0), (20, 30)))],
        [psg.Text("Login:", size=(6, 1), justification='right'), psg.Input(size=(30, 10), justification="center", key= "nome_login_atendente")],
        [psg.Text("Senha:", size=(6, 1), justification='right'), psg.Input(size=(30,10), justification="center", key= "senha_atendente", password_char='*')],
        [psg.Button("Logar", size=(20, 2), button_color=("white", "#2E8B57"), key="atendente_logou", pad=((0, 0), (10, 10)))],
        [psg.Button("Voltar", size=(12, 1), button_color=("white", "#000080"), key="voltar_login_atendente", pad=((0, 0), (20, 15)))]
    ]
    return psg.Window("Login de atendente", layout_login_atendente, background_color="white", element_justification='c')

def sistema_atendente():
    psg.theme('Reddit')
    layout_logado_atendente = [
        [psg.Text("Sistema de atendimento de compras por telefone",text_color='black', size=(40, 1), font=('Arial', 25), justification='center', pad=((0, 0), (0, 0)))],
        [psg.Button("Resgitrar usuário", size=(20, 2), button_color=("White", "#2E8B57"), key="registrar_usuario_atendente", pad=((0, 0), (10, 20)))],
        [psg.Text('CPF do cliente:', justification='right', size=(20,1)), psg.InputText(key='cpf'), psg.Button("Inserir CPF do cliente", key=("insere_cpf"))],

        #Camiseta
        [psg.Text("Camiseta - 30 R$",text_color='black', size=(20, 1), font=('Arial', 20), justification='center', pad=((0, 0), (30, 30))),
        psg.Listbox(["vermelha","verde","preta","azul","branca"],size=(20,4),select_mode=psg.LISTBOX_SELECT_MODE_SINGLE, key='lista_camiseta'), 
        psg.Text("Quantidade:"), psg.Input(default_text= '0' ,size=(10,1), key= "qtd_camiseta"),
        #Camisa
        psg.Text("Camisa - 40 R$",text_color='black', size=(20, 1), font=('Arial', 20), justification='center', pad=((0, 0), (20, 30))),
        psg.Listbox(["social preta","social branca","regata branca","regata estampada","polo preta"],size=(20,4),select_mode=psg.LISTBOX_SELECT_MODE_SINGLE, key='lista_camisa'), 
        psg.Text("Quantidade:"), psg.Input(default_text= '0' ,size=(10,1), key= "qtd_camisa")],

        #Casaco
        [psg.Text("Casaco - 75 R$",text_color='black', size=(20, 1), font=('Arial', 20), justification='center', pad=((0, 0), (20, 30))),
        psg.Listbox(["vermelho","branco","preto","verde"],size=(20,4),select_mode=psg.LISTBOX_SELECT_MODE_SINGLE, key='lista_casaco'), 
        psg.Text("Quantidade:"), psg.Input(default_text= '0' ,size=(10,1), key= "qtd_casaco"),
        #Cropped
        psg.Text("Cropped - 15 R$",text_color='black', size=(20, 1), font=('Arial', 20), justification='center', pad=((0, 0), (20, 30))),
        psg.Listbox(["vermelho","branco","preto","verde"],size=(20,4),select_mode=psg.LISTBOX_SELECT_MODE_SINGLE, key='lista_cropped'), 
        psg.Text("Quantidade:"), psg.Input(default_text= '0' ,size=(10,1), key= "qtd_cropped")],

        #Calça
        [psg.Text("Calça - 60 R$",text_color='black', size=(20, 1), font=('Arial', 20), justification='center', pad=((0, 0), (20, 30))),
        psg.Listbox(["vermelha","branca","preta","verde"],size=(20,4),select_mode=psg.LISTBOX_SELECT_MODE_SINGLE, key='lista_calça'), 
        psg.Text("Quantidade:"), psg.Input(default_text= '0' ,size=(10,1), key= "qtd_calça"),
        #Bermuda
        psg.Text("Bermuda - 50 R$",text_color='black', size=(20, 1), font=('Arial', 20), justification='center', pad=((0, 0), (20, 30))),
        psg.Listbox(["vermelha","branca","preta","verde"],size=(20,4),select_mode=psg.LISTBOX_SELECT_MODE_SINGLE, key='lista_bermuda'), 
        psg.Text("Quantidade:"), psg.Input(default_text= '0' ,size=(10,1), key= "qtd_bermuda")],
        
        #Saia
        [psg.Text("Saia - 120 R$",text_color='black', size=(20, 1), font=('Arial', 20), justification='center', pad=((0, 0), (20, 30))),
        psg.Listbox(["vermelha","branca","preta","verde"],size=(20,4),select_mode=psg.LISTBOX_SELECT_MODE_SINGLE, key='lista_saia'), 
        psg.Text("Quantidade:"), psg.Input(default_text= '0' ,size=(10,1), key= "qtd_saia"),
        #Tênis
        psg.Text("Tênis - 300 R$",text_color='black', size=(20, 1), font=('Arial', 20), justification='center', pad=((0, 0), (20, 30))),
        psg.Listbox(["vermelho","branco","preto","verde"],size=(20,4),select_mode=psg.LISTBOX_SELECT_MODE_SINGLE, key='lista_tênis'), 
        psg.Text("Quantidade:"), psg.Input(default_text= '0' ,size=(10,1), key= "qtd_tênis")],
        
        #Sapato
        [psg.Text("Sapato - 380 R$",text_color='black', size=(20, 1), font=('Arial', 20), justification='center', pad=((0, 0), (20, 30))),
        psg.Listbox(["vermelho","branco","preto","verde"],size=(20,4),select_mode=psg.LISTBOX_SELECT_MODE_SINGLE, key='lista_sapato'), 
        psg.Text("Quantidade:"), psg.Input(default_text= '0' ,size=(10,1), key= "qtd_sapato"),
        #Sapatilha
        psg.Text("Sapatilha - 200 R$",text_color='black', size=(20, 1), font=('Arial', 20), justification='center', pad=((0, 0), (20, 30))),
        psg.Listbox(["vermelha","branca","preta","verde"],size=(20,4),select_mode=psg.LISTBOX_SELECT_MODE_SINGLE, key='lista_sapatilha'), 
        psg.Text("Quantidade:"), psg.Input(default_text= '0' ,size=(10,1), key= "qtd_sapatilha")],

        [psg.Button("Adicionar ao Carrinho", size=(24, 2), button_color=("White", "Green"), key="adic_carrinho", pad=((0, 0), (10, 10)))],
        [psg.Button("Voltar", size=(12, 1), button_color=("white", "#000080"), key="voltar_login_atendente", pad=((0, 0), (10, 15)))]
    ]
    return psg.Window("Sistema Atendente", layout_logado_atendente, background_color="white", element_justification='c')

def janela_atendente_registrar_usuario():
    psg.theme('Reddit')
    layout_atendente_registrar_usuario = [
        [psg.Text("Sistema de cadastro de usuario",text_color='black', size=(30, 1), font=('Arial', 25), justification='center', pad=((0, 0), (20, 30)))],
        [psg.Text('Cadastro de Novo Usuário', font=('Arial', 25), justification='center', pad=((0,0), (20,30)))],
        [psg.Text('Nome:', justification='right', size=(10,1)), psg.InputText(key='nome'), psg.Text('(10-40 chars)')],
        [psg.Text('CPF:', justification='right', size=(10,1)), psg.InputText(key='cpf'), psg.Text('    (11 chars)')],
        [psg.Text('Bairro:', justification='right', size=(10,1)), psg.InputText(key='bairro'), psg.Text(' (3-40 chars)')],
        [psg.Text('Cidade:', justification='right', size=(10,1)), psg.InputText(key='cidade'), psg.Text(' (5-40 chars)')],
        [psg.Text('Estado:', justification='right', size=(10,1)), psg.InputText(key='estado'), psg.Text('      Sigla     ')],
        [psg.Button('Registrar', size=(20, 2), button_color=("white", "#2E8B57"), key="usuario_atendido_registrado")],
        [psg.Button("Voltar", size=(12, 1), button_color=("white", "#000080"), key="voltar_login_atendente", pad=((0, 0), (20, 15)))]
    ]
    return psg.Window("Atendente Registrar Usuario", layout_atendente_registrar_usuario, background_color="white", element_justification='c')

def janela_login_gerente():
    psg.theme('Reddit')
    layout_login_gerente = [
        [psg.Text("Login de gerente",text_color='black', size=(20, 1), font=('Arial', 25), justification='center', pad=((0, 0), (20, 30)))],
        [psg.Text("Login:", size=(6, 1), justification='right'), psg.Input(default_text="GerenciaLoja", size=(30, 10), justification="center", key= "nome_login_gerente")],
        [psg.Text("Senha:", size=(6, 1), justification='right'), psg.Input(default_text="gerente123", size=(30,10), justification="center", key= "senha_gerente", password_char='*')],
        [psg.Button("Logar", size=(20, 2), button_color=("white", "#2E8B57"), key="gerente_logou", pad=((0, 0), (10, 10)))],
        [psg.Button("Voltar", size=(12, 1), button_color=("white", "#000080"), key="voltar_login_gerente", pad=((0, 0), (20, 15)))]
    ]
    return psg.Window("Login de gerente", layout_login_gerente, background_color="white", element_justification='c')


def janela_registrar_atendente():
    psg.theme('Reddit')
    layout_registrar_atendente = [
        [psg.Text('Cadastro de Novo Usuário', font=('Arial', 25), justification='center', pad=((0,0), (20,30)))],
        [psg.Text('Nome:', justification='right', size=(10,1)), psg.InputText(key='nome_atendente'), psg.Text('(10-40 chars)')],
        [psg.Text('CPF:', justification='right', size=(10,1)), psg.InputText(key='cpf_atendente'), psg.Text('    (11 chars)')],
        [psg.Text('Senha:', justification='right', size=(10,1)), psg.InputText(key='senha_atendente', password_char='*'), psg.Text(' (8-20 chars)')],
        [psg.Button("Voltar", key='voltar_registrar_atendente', button_color=("white", "#000080"), size=(8, 2), pad=((0, 140), (25, 25))), psg.Button('Registrar', size=(20, 2), button_color=("white", "#2E8B57"), key="atendente_registrado")]
    ]
    return psg.Window("Registrar atendente", layout_registrar_atendente, element_justification='c')

def janela_excluir_atendente():
    psg.theme('Reddit')
    layout_excluir_atendente = [
        [psg.Text('Digite o CPF:', justification='right', size=(15,1)), psg.InputText(key='cpf_atendente'), psg.Text('    (11 chars)')],
        [psg.Button("excluir", key='excluir_atendente', button_color=("white", "red"), size=(8, 2), pad=((0, 140), (25, 25)))],
        [psg.Button("Voltar", key='voltar_excluir_atendente', button_color=("white", "#000080"), size=(8, 2), pad=((0, 140), (25, 25)))]
    ]
    return psg.Window("Registrar atendente", layout_excluir_atendente, element_justification='c')

def sistema_gerencia():
    psg.theme('Reddit')
    layout_sistema_gerencia = [
        [psg.Text("Sistema de Gestão de Loja", text_color='black', size=(20, 1), font=('Arial', 25), justification='center', pad=((0, 0), (20, 30)))],
        [psg.Button("Registrar Atendente", size=(18, 1), button_color=("white", "#000080"), key="registrar_atendente", pad=((0, 0), (20, 15)))],
        [psg.Button("Excluir Atendente", size=(18, 1), button_color=("white", "#000080"), key="excluir_atendente", pad=((0, 0), (20, 15)))],
        [psg.Button("Total de pedidos de uma conta", size=(25, 1), button_color=("white", "#000080"), key="todos_pedidos_conta", pad=((0, 0), (20, 15)))],
        [psg.Button("Total de pedidos de um carrinho", size=(25, 1), button_color=("white", "#000080"), key="todos_produtos_carrinho", pad=((0, 0), (20, 15)))],
        [psg.Button("Dados dos usuários cadastrados", size=(25, 1), button_color=("white", "#000080"), key="dados_usuarios_cadastrados", pad=((0, 0), (20, 15)))],
        [psg.Button("Médias anuais", size=(25, 1), button_color=("white", "#000080"), key="media_anual", pad=((0, 0), (20, 15)))],
        [psg.Button("Maior cliente", size=(25, 1), button_color=("white", "#000080"), key="maior_cliente", pad=((0, 0), (20, 15)))],
        [psg.Button("Dados das formas de pagamento", size=(25, 1), button_color=("white", "#000080"), key="formas_pagamento", pad=((0, 0), (20, 15)))],
        [psg.Button("Maior número de vendas", size=(25, 1), button_color=("white", "#000080"), key="maior_numero_vendas", pad=((0, 0), (20, 15)))],
        [psg.Button("Compra em todos os meses", size=(25, 1), button_color=("white", "#000080"), key="compras_todos_meses", pad=((0, 0), (20, 15)))],
        [psg.Button("Melhor atendente", size=(25, 1), button_color=("white", "#000080"), key="melhor_atendente", pad=((0, 0), (20, 15)))],
        [psg.Button("Filtrar usuários", size=(25,1), button_color=("white", "#000080"), key="filtrar_usuarios", pad=((0, 0), (20, 15)))],
        [psg.Button("Deslogar", size=(12, 1), button_color=("white", "red"), key="voltar_sistema_gerencia", pad=((0, 0), (20, 15)))]
    ]
    return psg.Window("Sistema gerencia", layout_sistema_gerencia, background_color="white", element_justification='c')

def sub_janela_total_pedido_conta_id():
    psg.theme('Reddit')
    layout_sistema_gerencia = [
        [psg.Text("Total de pedidos de uma conta", text_color='black', size=(30, 1), font=('Arial', 20), justification='center', pad=((0, 0), (20, 30)))],
        [psg.Text("ID conta:", size=(10, 1), justification='right'), psg.Input(size=(10, 10), justification="center", key= "id_conta",default_text="2")],
        [psg.Button("Enviar", key='enviar', button_color=("white", "Green"), size=(8, 2), pad=((0, 140), (25, 25)))],
        [psg.Button("Voltar", key='voltar_sistema_gerente', button_color=("white", "#000080"), size=(8, 2), pad=((0, 140), (25, 25)))]
    ]
    return psg.Window("Total_de_pedidos_de_uma_conta_id", layout_sistema_gerencia, background_color="white", element_justification='c')
def sub_janela_maior_cliente(cliente,total):
    psg.theme('Reddit')
    layout_maior_cliente = [
        [psg.Text(f"O melhor cliente é : {cliente}", text_color='black', size=(40, 1), font=('Arial', 20), justification='center', pad=((0, 0), (20, 30)))],
        [psg.Text(f"O total que ele já pagou é : {total} ", text_color='black', size=(40, 1), font=('Arial', 20), justification='center', pad=((0, 0), (20, 30)))],
        [psg.Button("Voltar", key='voltar_sistema_gerente', button_color=("white", "#000080"), size=(8, 2), pad=((0, 140), (25, 25)))]
    ]
    return psg.Window("Total_de_pedidos_de_uma_conta_id", layout_maior_cliente, background_color="white", element_justification='c')

def sub_janela_total_pedido_conta(total_pedidos):
    psg.theme('Reddit')
    # Criar a lista de layout do carrinho
    layout_sistema_total_pedidos = [
        [psg.Text("Total de pedidos de uma conta", text_color='black', size=(30, 1), font=('Arial', 22), justification='center', pad=((0, 0), (20, 30)))],
    ]
    for id, status, data,cpf_atendente in total_pedidos:
        layout_sistema_total_pedidos.extend([
                [psg.Text(f"ID: {id}, Status: {status}, Data: {data}, CPF_atendente: {cpf_atendente}", size=(100, 1), justification='center')],
        ])
    layout_sistema_total_pedidos.extend([
        [psg.Button("Voltar", key='voltar_sistema_gerente', button_color=("white", "#000080"), size=(8, 2), pad=((0, 140), (25, 25)))]
    ]
    )
    return psg.Window("Total_de_pedidos_de_uma_conta", layout_sistema_total_pedidos, background_color="white", element_justification='c')
def sub_todos_produtos_carrinho_id():
    psg.theme('Reddit')
    layout_sub_todos_produtos_carrinho_id = [
        [psg.Text("Total de produtos de um carrinho", text_color='black', size=(30, 1), font=('Arial', 20), justification='center', pad=((0, 0), (20, 30)))],
        [psg.Text("ID carrinho:", size=(10, 1), justification='right'), psg.Input(size=(10, 10), justification="center", key= "id_carrinho",default_text="2")],
        [psg.Button("Enviar", key='enviar', button_color=("white", "Green"), size=(8, 2), pad=((0, 140), (25, 25)))],
        [psg.Button("Voltar", key='voltar_sistema_gerente', button_color=("white", "#000080"), size=(8, 2), pad=((0, 140), (25, 25)))]
    ]
    return psg.Window("Total de pedidos de uma conta id", layout_sub_todos_produtos_carrinho_id, background_color="white", element_justification='c')

def sub_todos_produtos_carrinho(total_produtos):
    psg.theme('Reddit')
    layout_sub_todos_produtos_carrinho= [
        [psg.Text("Total de produtos de um carrinho", text_color='black', size=(30, 1), font=('Arial', 22), justification='center', pad=((0, 0), (20, 30)))],
    ]
    for id_conta_carrinho_de_compras, id_item, valor, nome in total_produtos:
        layout_sub_todos_produtos_carrinho.extend([
                [psg.Text(f"ID da conta : {id_conta_carrinho_de_compras}, ID do item: {id_item},valor: {valor}, nome: {nome}", size=(100, 1), justification='center')],
        ])
    layout_sub_todos_produtos_carrinho.extend([
        [psg.Button("Voltar", key='voltar_sistema_gerente', button_color=("white", "#000080"), size=(8, 2), pad=((0, 140), (25, 25)))]
    ])
    return psg.Window("Total de pedidos de uma conta id", layout_sub_todos_produtos_carrinho, background_color="white", element_justification='c')
def sub_janela_media_anual(media_anual):
    psg.theme('Reddit')
    sub_janela_media_anual = [
        [psg.Text("Média anual", text_color='black', size=(30, 1), font=('Arial', 22), justification='center', pad=((0, 0), (20, 30)))],
    ]
    for ano,media in media_anual:
        sub_janela_media_anual.extend([
                [psg.Text(f"Ano : {ano}, média : {media:.2f}", size=(100, 1), justification='center')],
        ])
    sub_janela_media_anual.extend([
    [psg.Button("Voltar", key='voltar_sistema_gerente', button_color=("white", "#000080"), size=(8, 2), pad=((0, 140), (25, 25)))]
    ]
    )

    return psg.Window("Média anual", sub_janela_media_anual, background_color="white", element_justification='c')
def sub_janela_dados_usuarios(quantidade_usuarios_web, quantidade_usuarios_atendidos):
    psg.theme('Reddit')
    layout_sistema_gerencia = [
        [psg.Text("Dados dos usuários cadastrados", text_color='black', size=(30, 1), font=('Arial', 22), justification='center', pad=((0, 0), (20, 30)))],
        [psg.Text(f"Total de usuários cadastrados: {quantidade_usuarios_web + quantidade_usuarios_atendidos}", size=(34, 1), justification='center', font=('Arial', 12))],
        [psg.Text(f"Quantidade de usuários web: {quantidade_usuarios_web}", size=(34, 1), justification='center', font=('Arial', 12))],
        [psg.Text(f"Quantidade de usuários atendidos: {quantidade_usuarios_atendidos}", size=(40, 1), justification='center', font=('Arial', 12))],
        [psg.Text("Dados dos clientes:", size=(20, 1), justification='center', font=('Arial', 18), pad=((0,0),(20,20)))],
        [psg.Button("Mostrar dados", button_color=("white", "#000080"), size=(14, 2), pad=((0, 0), (0, 25)))],
        [psg.Output(size=(50,10))],
        [psg.Button("Voltar", key='voltar_sistema_gerente', button_color=("white", "#000080"), size=(14, 2), pad=((0, 0), (25, 25)))]
    ]
    return psg.Window("Dados_dos_usuários_cadastrados", layout_sistema_gerencia, background_color="white", element_justification='c')

def sub_janela_dados_usuarios(quantidade_usuarios_web, quantidade_usuarios_atendidos):
    psg.theme('Reddit')
    layout_sistema_gerencia = [
        [psg.Text("Dados dos usuários cadastrados", text_color='black', size=(30, 1), font=('Arial', 22), justification='center', pad=((0, 0), (20, 30)))],
        [psg.Text(f"Total de usuários cadastrados: {quantidade_usuarios_web + quantidade_usuarios_atendidos}", size=(34, 1), justification='center', font=('Arial', 12))],
        [psg.Text(f"Quantidade de usuários web: {quantidade_usuarios_web}", size=(34, 1), justification='center', font=('Arial', 12))],
        [psg.Text(f"Quantidade de usuários atendidos: {quantidade_usuarios_atendidos}", size=(40, 1), justification='center', font=('Arial', 12))],
        [psg.Text("Dados dos clientes:", size=(20, 1), justification='center', font=('Arial', 18), pad=((0,0),(20,20)))],
        [psg.Button("Mostrar dados", button_color=("white", "#000080"), size=(14, 2), pad=((0, 0), (0, 25)))],
        [psg.Output(size=(50,10))],
        [psg.Button("Voltar", key='voltar_sistema_gerente', button_color=("white", "#000080"), size=(14, 2), pad=((0, 0), (25, 25)))]
    ]
    return psg.Window("Dados_dos_usuários_cadastrados", layout_sistema_gerencia, background_color="white", element_justification='c')

def sub_janela_pagamento_mais_utilizado(forma_pagamento, quantidade_pagamento, valor_pagamento):
    psg.theme('Reddit')
    layout_sistema_gerencia = [
        [psg.Text("Dados sobre pagamento", text_color='black', size=(36, 1), font=('Arial', 22), justification='center', pad=((0, 0), (20, 30)))],
        [psg.Text(f"A forma de pagamento mais utilizada é no {forma_pagamento[0]}:", text_color='black', size=(50, 1), font=('Arial', 16), justification='left', pad=((0, 0), (0, 0)))],
        [psg.Text(f"Pagamentos: {quantidade_pagamento[0]}    Valor: {valor_pagamento[0]} reais", text_color='black', size=(30, 1), font=('Arial', 14), justification='left', pad=((40, 0), (0, 0)))],
        [psg.Text(f"A segunda forma de pagamento mais utilizada é no {forma_pagamento[1]}:", text_color='black', size=(50, 1), font=('Arial', 16), justification='left', pad=((0, 0), (20, 0)))],
        [psg.Text(f"Pagamentos: {quantidade_pagamento[1]}    Valor: {valor_pagamento[1]} reais", text_color='black', size=(30, 1), font=('Arial', 14), justification='left', pad=((40, 0), (0, 0)))],
        [psg.Text(f"A terceira forma de pagamento mais utilizada é no {forma_pagamento[2]}:", text_color='black', size=(50, 1), font=('Arial', 16), justification='left', pad=((0, 0), (20, 0)))],
        [psg.Text(f"Pagamentos: {quantidade_pagamento[2]}    Valor: {valor_pagamento[2]} reais", text_color='black', size=(30, 1), font=('Arial', 14), justification='left', pad=((40, 0), (0, 0)))],
        [psg.Text(f"A forma de pagamento menos utilizada é no {forma_pagamento[3]}:", text_color='black', size=(50, 1), font=('Arial', 16), justification='left', pad=((0, 0), (20, 0)))],
        [psg.Text(f"Pagamentos: {quantidade_pagamento[3]}    Valor: {valor_pagamento[3]} reais", text_color='black', size=(30, 1), font=('Arial', 14), justification='left', pad=((40, 0), (0, 0)))],
        [psg.Button("Voltar", key='voltar_sistema_gerente', button_color=("white", "#000080"), size=(14, 2), pad=((0, 0), (25, 25)))]
    ]
    return psg.Window("Dados sobre pagamento", layout_sistema_gerencia, background_color="white", element_justification='l')

def sub_janela_maior_numero_vendas(maior_num_ano, maior_num_mes):
    psg.theme('Reddit')
    layout_sistema_gerencia = [
        [psg.Text("Dados de vendas", text_color='black', size=(36, 1), font=('Arial', 22), justification='center', pad=((0, 0), (20, 30)))],
        [psg.Text(f"O ano com o maior número de vendas foi: {maior_num_ano}", text_color='black', size=(50, 1), font=('Arial', 14), justification='left', pad=((40, 0), (0, 0)))],
        [psg.Text(f"O mês com o maior número de vendas foi o mês: {maior_num_mes}", text_color='black', size=(50, 1), font=('Arial', 14), justification='left', pad=((40, 0), (0, 0)))],
        [psg.Button("Voltar", key='voltar_sistema_gerente', button_color=("white", "#000080"), size=(14, 2), pad=((0, 0), (25, 25)))]
    ]
    return psg.Window("Dados de vendas", layout_sistema_gerencia, background_color="white", element_justification='c')

def sub_janela_compras_todos_meses():
    psg.theme('Reddit')
    layout_sistema_gerencia = [
        [psg.Text("Compras em todos os meses", text_color='black', size=(36, 1), font=('Arial', 22), justification='center', pad=((0, 0), (20, 30)))],
        [psg.Text('Insira o ano para verificar:', justification='center', size=(30,1), font=('Arial', 14)), psg.InputText(key='ano'), psg.Button("Procurar", key="busca_compra")],
        [psg.Text("CPF dos usuários:"), psg.Output(size=(30,5), key= "output", pad=((0,0),(20,20)))],
        [psg.Button("Voltar", key='voltar_sistema_gerente', button_color=("white", "#000080"), size=(14, 2), pad=((0, 0), (25, 25)))]
    ]
    return psg.Window("Compra em todos os meses", layout_sistema_gerencia, background_color="white", element_justification='c')

def sub_janela_melhor_atendente(cpf_atendente, quantidade_vendas):
    psg.theme('Reddit')
    layout_sistema_gerencia = [
        [psg.Text(f"Melhor atendente", text_color='black', size=(40, 1), font=('Arial', 22), justification='center', pad=((0, 0), (20, 30)))],
        [psg.Text(f"O atendente que mais vendeu foi o {cpf_atendente} com {quantidade_vendas} vendas.", size=(60,1), font=('Arial', 12))],
        [psg.Button("Voltar", key='voltar_sistema_gerente', button_color=("white", "#000080"), size=(14, 2), pad=((0, 0), (25, 25)))]
    ]
    return psg.Window("Melhor atendente", layout_sistema_gerencia, background_color="white", element_justification='c')

def sub_janela_filtrar_usuarios():
    psg.theme('Reddit')
    layout_sistema_gerencia = [
        [psg.Text(f"Filtrar usuários", text_color='black', size=(40, 1), font=('Arial', 22), justification='center', pad=((0, 0), (20, 30)))],
        [psg.Text('Bairro:', justification='right', size=(10,1)), psg.InputText(key='bairro'), psg.Text(' (3-40 chars)')],
        [psg.Text('Cidade:', justification='right', size=(10,1)), psg.InputText(key='cidade'), psg.Text(' (5-40 chars)')],
        [psg.Text('Estado:', justification='right', size=(10,1)), psg.InputText(key='estado'), psg.Text('      Sigla     ')],
        [psg.Text('Resultados', justification='center',  font=('Arial', 16), size=(10,1), pad=((0,0),(20,0)))],
        [psg.Output(size=(34,10), key="output", pad=((0,0),(10,10)))],
        [psg.Button("Pesquisar", key="pesquisar", button_color=("white", "#000080"), size=(14, 2), pad=((0, 0), (25, 25))), 
        psg.Button("Voltar", key='voltar_sistema_gerente', button_color=("white", "#000080"), size=(14, 2), pad=((0, 0), (25, 25)))]
    ]
    return psg.Window("Filtrar_usuários", layout_sistema_gerencia, background_color="white", element_justification='c')


def pagamento(total_carrinho):
    psg.theme('Reddit')
    fonte_titulo = ('Arial', 30)
    fonte_texto = ('Arial', 15)
    cor_botao = ('white', '#008C8C')

    layout_pagamento = [
        [psg.Text("Janela de Pagamento", text_color='black', font=fonte_titulo, justification='center', pad=((0,0),(10,20)))],
        [psg.Text("Valor do carrinho:", font=fonte_texto, justification='center'), psg.Text(f"{total_carrinho} reais", size=(20, 1), key='total_carrinho', font=fonte_texto)],
        [psg.Text("Formas de pagamento:", font=fonte_texto, justification='center',pad=((0,0),(10,20))), psg.Text(size=(10, 1), key='forma_pagamento', font=fonte_texto, pad=((0,0),(10,20)))],
        [
            psg.Button('Pix', button_color=cor_botao, size=(10, 2)),
            psg.Button('Débito', button_color=cor_botao, size=(10, 2)),
            psg.Button('Crédito', button_color=cor_botao, size=(10, 2)),
            psg.Button('Boleto', button_color=cor_botao, size=(10, 2))
        ],
        [psg.Text("Quantidade de parcelas:", font=fonte_texto, pad=((0,0),(20,20))), psg.InputText(default_text= '1', size=(10, 1), key='parcela', font=fonte_texto, pad=((0,0),(20,20)))],
        [psg.Button('Pagar', size=(20, 2)), psg.Button('Cancelar pagamento', button_color=('white', '#FF5733'), size=(20, 2))]
    ]
    return psg.Window("Sistema de Pagamento", layout_pagamento, background_color="white", element_justification='c')

def conecta(host,user,password):
    # Conectar ao MySQL
    try:
        connection = mysql.connector.connect(host=host, user=user, password=password)
        if (connection):
            return connection
    except:
        print("Não consegui me conectar")
        return 0