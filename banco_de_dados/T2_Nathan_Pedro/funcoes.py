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
    
def janela_login_usuario():
    psg.theme('Reddit')
    layout_login_usuario = [
        [psg.Text("Login de usuário",text_color='black', size=(20, 1), font=('Arial', 25), justification='center', pad=((0, 0), (20, 30)))],
        [psg.Text("Login:", size=(6, 1), justification='right'), psg.Input(size=(30, 10), justification="center", key= "nome_login_usuario")],
        [psg.Text("Senha:", size=(6, 1), justification='right'), psg.Input(size=(30,10), justification="center", key= "senha_usuario", password_char='*')],
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
        [psg.Text("Atendente",text_color='black', size=(20, 1), font=('Arial', 25), justification='center', pad=((0, 0), (20, 30)))],
        [psg.Button("Resgitrar usuário", size=(20, 2), button_color=("White", "#2E8B57"), key="registrar_usuario_atendente", pad=((0, 0), (10, 10)))],
        [psg.Button("Voltar", size=(12, 1), button_color=("white", "#000080"), key="voltar_login_atendente", pad=((0, 0), (20, 15)))]
    ]
    return psg.Window("Atendente", layout_logado_atendente, background_color="white", element_justification='c')

def janela_atendente_registrar_usuario():
    psg.theme('Reddit')
    layout_atendente_registrar_usuario = [
        [psg.Text("Atendente",text_color='black', size=(20, 1), font=('Arial', 25), justification='center', pad=((0, 0), (20, 30)))],
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


def conecta(host,user,password):
    # Conectar ao MySQL
    try:
        connection = mysql.connector.connect(host=host, user=user, password=password)
        if (connection):
            return connection
    except:
        print("Não consegui me conectar")
        return 0