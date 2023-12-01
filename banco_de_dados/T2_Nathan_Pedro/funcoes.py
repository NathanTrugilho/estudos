import PySimpleGUI as psg
import mysql.connector

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
        psg.Button("Ver carrinho", size=(20, 2), button_color=("White", "Green"), key="ver_carrinho", pad=((0, 0), (10, 10)))],
        #[psg.Image('camisapreta.jpg',expand_x=True, expand_y=True ),psg.Text("Camisa preta")],
        [psg.Text("Camisa",text_color='black', size=(20, 1), font=('Arial', 25), justification='center', pad=((0, 0), (20, 30))),
        psg.Listbox(["camisa social preta","camisa social branca","camisa regata branca","camisa regata estampada","camisa polo preta"],size=(20,4),select_mode=psg.LISTBOX_SELECT_MODE_SINGLE), 
        psg.Text("Quantidade:"), psg.Input(size=(10,1), key= "qtd_camisa"),
        psg.Button("Adicionar ao Carrinho", size=(20, 2), button_color=("White", "Green"), key="comprar1", pad=((0, 0), (10, 10)))],

        [psg.Text("Camiseta",text_color='black', size=(20, 1), font=('Arial', 25), justification='center', pad=((0, 0), (20, 30))),
        psg.Listbox(["camiseta vermelha","camiseta verde"," camiseta preta","camiseta azul","camiseta branca"],size=(20,4),select_mode=psg.LISTBOX_SELECT_MODE_SINGLE), psg.Text("Quantidade:"), psg.Input(size=(10,1), key= "qtd_camiseta"),
        psg.Button("Adicionar ao Carrinho", size=(20, 2), button_color=("White", "Green"), key="comprar2", pad=((0, 0), (10, 10)))],
        
        [psg.Text("casaco",text_color='black', size=(20, 1), font=('Arial', 25), justification='center', pad=((0, 0), (20, 30))),
        psg.Listbox(["casaco vermelho","casaco branco","casaco preto","casaco verde"],size=(20,4),select_mode=psg.LISTBOX_SELECT_MODE_SINGLE), psg.Text("Quantidade:"), psg.Input(size=(10,1), key= "qtd_casaco"),
        psg.Button("Adicionar ao Carrinho", size=(20, 2), button_color=("White", "Green"), key="comprar3", pad=((0, 0), (10, 10)))],

        [psg.Text("cropped",text_color='black', size=(20, 1), font=('Arial', 25), justification='center', pad=((0, 0), (20, 30))),
        psg.Listbox(["cropped vermelho"," cropped preto","cropped branco","cropped verde"],size=(20,4),select_mode=psg.LISTBOX_SELECT_MODE_SINGLE), psg.Text("Quantidade:"), psg.Input(size=(10,1), key= "qtd_cropped"),
        psg.Button("Adicionar ao Carrinho", size=(20, 2), button_color=("White", "Green"), key="comprar4", pad=((0, 0), (10, 10)))],
        
        [psg.Text("calça",text_color='black', size=(20, 1), font=('Arial', 25), justification='center', pad=((0, 0), (20, 30))),
        psg.Listbox(["calça vermelha","calça preta","calça branca","calça verde"],size=(20,4),select_mode=psg.LISTBOX_SELECT_MODE_SINGLE), psg.Text("Quantidade:"), psg.Input(size=(10,1), key= "qtd_calça"),
        psg.Button("Adicionar ao Carrinho", size=(20, 2), button_color=("White", "Green"), key="comprar5", pad=((0, 0), (10, 10)))],
       
        [psg.Text("bermuda",text_color='black', size=(20, 1), font=('Arial', 25), justification='center', pad=((0, 0), (20, 30))),
        psg.Listbox(["bermuda vermelha","bermuda preta","bermuda branca","bermuda verde"],size=(20,4),select_mode=psg.LISTBOX_SELECT_MODE_SINGLE), psg.Text("Quantidade:"), psg.Input(size=(10,1), key= "qtd_bermuda"),
        psg.Button("Adicionar ao Carrinho", size=(20, 2), button_color=("White", "Green"), key="comprar6", pad=((0, 0), (10, 10)))],
        
        [psg.Text("saia",text_color='black', size=(20, 1), font=('Arial', 25), justification='center', pad=((0, 0), (20, 30))),
        psg.Listbox(["saia vermelha","saia preta","saia branca","saia verde"],size=(20,4),select_mode=psg.LISTBOX_SELECT_MODE_SINGLE), psg.Text("Quantidade:"), psg.Input(size=(10,1), key= "qtd_saia"),
        psg.Button("Adicionar ao Carrinho", size=(20, 2), button_color=("White", "Green"), key="comprar7", pad=((0, 0), (10, 10)))],
        
        [psg.Text("tênis",text_color='black', size=(20, 1), font=('Arial', 25), justification='center', pad=((0, 0), (20, 30))),
        psg.Listbox(["tênis vermelho","tênis preta","tênis branca","tênis verde"],size=(20,4),select_mode=psg.LISTBOX_SELECT_MODE_SINGLE), psg.Text("Quantidade:"), psg.Input(size=(10,1), key= "qtd_tênis"),
        psg.Button("Adicionar ao Carrinho", size=(20, 2), button_color=("White", "Green"), key="comprar8", pad=((0, 0), (10, 10)))],
        
        [psg.Text("sapato",text_color='black', size=(20, 1), font=('Arial', 25), justification='center', pad=((0, 0), (20, 30))),
        psg.Listbox(["sapato vermelho","sapato preta","sapato branca","sapato verde"],size=(20,4),select_mode=psg.LISTBOX_SELECT_MODE_SINGLE), psg.Text("Quantidade:"), psg.Input(size=(10,1), key= "qtd_sapato"),
        psg.Button("Adicionar ao Carrinho", size=(20, 2), button_color=("White", "Green"), key="comprar9", pad=((0, 0), (10, 10)))],
       
        [psg.Text("sapatilha",text_color='black', size=(20, 1), font=('Arial', 25), justification='center', pad=((0, 0), (20, 30))),
        psg.Listbox(["sapatilha vermelha","sapatilha preta","sapatilha branca","sapatilha verde"],size=(20,4),select_mode=psg.LISTBOX_SELECT_MODE_SINGLE), psg.Text("Quantidade:"), psg.Input(size=(10,1), key= "qtd_sapatilha"),
        psg.Button("Adicionar ao Carrinho", size=(20, 2), button_color=("White", "Green"), key="comprar10", pad=((0, 0), (10, 10)))]


    ]
    return psg.Window("Login de usuário", layout_sistema_usuario, background_color="white", element_justification='c')

def janela_carrinho(compras):
    psg.theme('Reddit')
    layout_carrinho = [
        [psg.Text("Carrinho",text_color='black', size=(20, 1), font=('Arial', 25), justification='center', pad=((0, 0), (20, 30)))],
    ]
    for nome,qtd in compras: 
        layout_carrinho.extend([  # Use extend para adicionar elementos à lista principal
            [psg.Text(nome,size=(30, 1), justification='right'),psg.Text(qtd,size=(6, 1), justification='right')],
        ])
    layout_carrinho.extend([ 
        [psg.Button("Comprar", size=(12, 1), button_color=("white", "green"), key="comprar_carrinho", pad=((0, 0), (20, 15)))],
        [psg.Button("Voltar", size=(12, 1), button_color=("white", "#000080"), key="voltar_sistema_usuario", pad=((0, 0), (20, 15)))],
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
        [psg.Text("Login:", size=(6, 1), justification='right'), psg.Input(size=(30, 10), justification="center", key= "nome_login_atendente", default_text="Luiz Silva")],
        [psg.Text("Senha:", size=(6, 1), justification='right'), psg.Input(size=(30,10), justification="center", key= "senha_atendente", password_char='*', default_text="78901244")],
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
        [psg.Text("Camiseta",text_color='black', size=(20, 1), font=('Arial', 20), justification='center', pad=((0, 0), (30, 30))),
        psg.Listbox(["vermelha","verde","preta","azul","branca"],size=(20,4),select_mode=psg.LISTBOX_SELECT_MODE_SINGLE, key='lista_camiseta'), 
        psg.Text("Quantidade:"), psg.Input(default_text= "0" ,size=(10,1), key= "qtd_camiseta"),
        #Camisa
        psg.Text("Camisa",text_color='black', size=(20, 1), font=('Arial', 20), justification='center', pad=((0, 0), (20, 30))),
        psg.Listbox(["social preta","social branca","regata branca","regata estampada","polo preta"],size=(20,4),select_mode=psg.LISTBOX_SELECT_MODE_SINGLE, key='lista_camisa'), 
        psg.Text("Quantidade:"), psg.Input(default_text= "0" ,size=(10,1), key= "qtd_camisa")],

        #Casaco
        [psg.Text("Casaco",text_color='black', size=(20, 1), font=('Arial', 20), justification='center', pad=((0, 0), (20, 30))),
        psg.Listbox(["vermelho","branco","preto","verde"],size=(20,4),select_mode=psg.LISTBOX_SELECT_MODE_SINGLE, key='lista_casaco'), 
        psg.Text("Quantidade:"), psg.Input(default_text= "0" ,size=(10,1), key= "qtd_casaco"),
        #Cropped
        psg.Text("Cropped",text_color='black', size=(20, 1), font=('Arial', 20), justification='center', pad=((0, 0), (20, 30))),
        psg.Listbox(["vermelho","branco","preto","verde"],size=(20,4),select_mode=psg.LISTBOX_SELECT_MODE_SINGLE, key='lista_cropped'), 
        psg.Text("Quantidade:"), psg.Input(default_text= "0" ,size=(10,1), key= "qtd_cropped")],

        #Calça
        [psg.Text("Calça",text_color='black', size=(20, 1), font=('Arial', 20), justification='center', pad=((0, 0), (20, 30))),
        psg.Listbox(["vermelha","branca","preta","verde"],size=(20,4),select_mode=psg.LISTBOX_SELECT_MODE_SINGLE, key='lista_calça'), 
        psg.Text("Quantidade:"), psg.Input(default_text= "0" ,size=(10,1), key= "qtd_calça"),
        #Bermuda
        psg.Text("Bermuda",text_color='black', size=(20, 1), font=('Arial', 20), justification='center', pad=((0, 0), (20, 30))),
        psg.Listbox(["vermelha","branca","preta","verde"],size=(20,4),select_mode=psg.LISTBOX_SELECT_MODE_SINGLE, key='lista_bermuda'), 
        psg.Text("Quantidade:"), psg.Input(default_text= "0" ,size=(10,1), key= "qtd_bermuda")],
        
        #Saia
        [psg.Text("Saia",text_color='black', size=(20, 1), font=('Arial', 20), justification='center', pad=((0, 0), (20, 30))),
        psg.Listbox(["vermelha","branca","preta","verde"],size=(20,4),select_mode=psg.LISTBOX_SELECT_MODE_SINGLE, key='lista_saia'), 
        psg.Text("Quantidade:"), psg.Input(default_text= "0" ,size=(10,1), key= "qtd_saia"),
        #Tênis
        psg.Text("Tênis",text_color='black', size=(20, 1), font=('Arial', 20), justification='center', pad=((0, 0), (20, 30))),
        psg.Listbox(["vermelho","branco","preto","verde"],size=(20,4),select_mode=psg.LISTBOX_SELECT_MODE_SINGLE, key='lista_tênis'), 
        psg.Text("Quantidade:"), psg.Input(default_text= "0" ,size=(10,1), key= "qtd_tênis")],
        
        #Sapato
        [psg.Text("Sapato",text_color='black', size=(20, 1), font=('Arial', 20), justification='center', pad=((0, 0), (20, 30))),
        psg.Listbox(["vermelho","branco","preto","verde"],size=(20,4),select_mode=psg.LISTBOX_SELECT_MODE_SINGLE, key='lista_sapato'), 
        psg.Text("Quantidade:"), psg.Input(default_text= "0" ,size=(10,1), key= "qtd_sapato"),
        #Sapatilha
        psg.Text("Sapatilha",text_color='black', size=(20, 1), font=('Arial', 20), justification='center', pad=((0, 0), (20, 30))),
        psg.Listbox(["vermelha","branca","preta","verde"],size=(20,4),select_mode=psg.LISTBOX_SELECT_MODE_SINGLE, key='lista_sapatilha'), 
        psg.Text("Quantidade:"), psg.Input(default_text= "0" ,size=(10,1), key= "qtd_sapatilha")],

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
        [psg.Text("Login:", size=(6, 1), justification='right'), psg.Input(size=(30, 10), justification="center", key= "nome_login_gerente")],
        [psg.Text("Senha:", size=(6, 1), justification='right'), psg.Input(size=(30,10), justification="center", key= "senha_gerente", password_char='*')],
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

def sistema_gerencia():
    psg.theme('Reddit')
    layout_sistema_gerencia = [
        [psg.Text("Sistema de Gestão de Loja", text_color='black', size=(20, 1), font=('Arial', 25), justification='center', pad=((0, 0), (20, 30)))],
        [psg.Button("Registrar Atendente", size=(18, 1), button_color=("white", "#000080"), key="registrar_atendente", pad=((0, 0), (20, 15)))],
        [psg.Button("Deslogar", size=(12, 1), button_color=("white", "red"), key="voltar_sistema_gerencia", pad=((0, 0), (20, 15)))]
    ]
    return psg.Window("Sistema gerencia", layout_sistema_gerencia, background_color="white", element_justification='c')

def pagamento():
    psg.theme('Reddit')
    fonte_titulo = ('Arial', 30)
    fonte_texto = ('Arial', 15)
    cor_botao = ('white', '#008C8C')

    layout_pagamento = [
        [psg.Text("Janela de Pagamento", text_color='black', font=fonte_titulo, justification='center', pad=((0,0),(10,20)))],
        [psg.Text("Valor do carrinho: ", font=fonte_texto, justification='center'), psg.Text(size=(10, 1), key='-VALOR-', font=fonte_texto)],
        [psg.Text("Formas de pagamento:", font=fonte_texto, justification='center',pad=((0,0),(10,20))), psg.Text(size=(10, 1), key='forma_pagamento', font=fonte_texto)],
        [
            psg.Button('Pix', button_color=cor_botao, size=(10, 2)),
            psg.Button('Débito', button_color=cor_botao, size=(10, 2)),
            psg.Button('Crédito', button_color=cor_botao, size=(10, 2)),
            psg.Button('Boleto', button_color=cor_botao, size=(10, 2))
        ],
        [psg.Text("Quantidade de parcelas:", font=fonte_texto, pad=((0,0),(20,20))), psg.InputText(size=(5, 1), key='-PARCELAS-', font=fonte_texto, pad=((0,0),(20,20)))],
        [psg.Button('Pagar', size=(20, 2)), psg.Button('Voltar', button_color=('white', '#FF5733'), size=(20, 2))]
    ]
    janela = psg.Window("Sistema de Pagamento", layout_pagamento, background_color="white", element_justification='c')

    while True:
        event, values = janela.read()

        if event == psg.WIN_CLOSED:
            break
        elif event in ('Pix', 'Débito', 'Crédito', 'Boleto'):
            janela['forma_pagamento'].update(f"{event}")
        elif event == 'Pagar':
            parcelas = values['-PARCELAS-']
            # Lógica para pagamento com a quantidade de parcelas selecionada
            psg.popup(f"Pagamento realizado em {parcelas} vezes.")

    janela.close()

def conecta(host,user,password):
    # Conectar ao MySQL
    try:
        connection = mysql.connector.connect(host=host, user=user, password=password)
        if (connection):
            return connection
    except:
        print("Não consegui me conectar")
        return 0