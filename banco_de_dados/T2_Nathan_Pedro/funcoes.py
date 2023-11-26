import PySimpleGUI as sg
import mysql.connector

def janela_login():
    sg.theme('Reddit')
    layout_login = [
        [sg.Text("Meu Banco de Dados", size=(20, 1), font=('Arial', 25), justification='center', pad=((0, 0), (30, 20)))],
        [sg.Button("Login como Usuário", size=(30, 2), button_color=("white", "#6495ED"), key="login_usuario", pad=((0, 0), (10, 5)))],
        [sg.Text("Registrar conta", size=(12, 1), text_color='#000080', enable_events=True, key="registrar_usuario", justification='center', pad=((0, 0),(0, 15)))],
        [sg.Button("Login como Atendente", size=(30, 2), button_color=("white", "#6495ED"), key="login_atendente", pad=((0, 0), (10, 10)))],
        [sg.Button("Sair", size=(12, 1), button_color=("white", "red"), key="sair", pad=((0, 0), (20, 15)))]
        
    ]
    return sg.Window("Login", layout_login, background_color="white", element_justification='c')


def janela_login_usuario():
    sg.theme('Reddit')
    layout_login_usuario = [
        [sg.Text("Login Usuário",text_color='blue', size=(20, 1), font=('Arial', 25), justification='center', pad=((0, 0), (30, 20)))],
        [sg.Input("Nome", size=(30, 10), justification="center", key= "nome")],
        [sg.Input("Senha", size=(30,10), justification="center", key= "senha")],
        [sg.Button("Logar", size=(30, 2), button_color=("white", "#6495ED"), key="usuario_logou", pad=((0, 0), (10, 10)))],
        [sg.Button("Voltar", size=(12, 1), button_color=("white", "red"), key="voltar", pad=((0, 0), (20, 15)))],
    ]
    return sg.Window("Login usuário", layout_login_usuario, background_color="white", element_justification='c')

def janela_registrar_usuario():
    sg.theme('Reddit')
    layout_registrar_usuario = [
        [sg.Text('Cadastro de Novo Usuário', font=('Helvetica', 25), justification='center', pad=((50,50), (20,20)))],
        [sg.InputText(key='nome', default_text='Nome')],
        [sg.InputText(key='login', default_text='Login')],
        [sg.InputText(key='senha', default_text='Senha', password_char='*')],
        [sg.InputText(key='cpf', default_text='CPF')],
        [sg.InputText(key='bairro', default_text='Bairro')],
        [sg.InputText(key='estado', default_text='Estado')],
        [sg.InputText(key='cidade', default_text='Cidade')],
        [sg.Button("Voltar", key='voltar', button_color=("white", "#000080"), size=(4, 1), pad=((0, 140), (25, 25))), sg.Button('Registrar', size=(16, 2), button_color=("white", "green"), key="registrado")]
    ]
    return sg.Window("Login de usuario", layout_registrar_usuario, element_justification= 'c')
    
def janela_login_atendente():
    sg.theme('Reddit')
    layout_login_atendente = [
        [sg.Text("Login Atendente",text_color='blue', size=(20, 1), font=('Arial', 25), justification='center', pad=((0, 0), (30, 20)))],
        [sg.Input("Nome", size=(30, 10), justification="center")],
        [sg.Input("Senha", size=(30,10), justification="center")],
        [sg.Button("Logar", size=(30, 2), button_color=("white", "#6495ED"), key="login", pad=((0, 0), (10, 10)))],
        [sg.Button("Voltar", size=(12, 1), button_color=("white", "red"), key="voltar", pad=((0, 0), (20, 15)))]
    ]
    return sg.Window("Login atendente", layout_login_atendente, background_color="white", element_justification='c')

def verifica_bd():
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

    cursor = connection.cursor()
    cursor.execute("use loja;")

    cursor.execute("show tables like 'usuario'")
    tables = cursor.fetchone()

    if not tables:
        # Criar a tabela
        cursor.execute("""
            CREATE TABLE usuario (
                cpf CHAR(11) NOT NULL PRIMARY KEY,
                bairro VARCHAR(50) NOT NULL,
                cidade VARCHAR(50) NOT NULL,
                estado VARCHAR(2) NOT NULL,
                nome VARCHAR(30) NOT NULL
            )
        """)

        cursor.execute("""INSERT INTO usuario (cpf, bairro, cidade, estado, nome)
            VALUES ('11122233344', 'Centro', 'São Paulo', 'SP', 'João'),
        ('22233344455', 'Bairro 1', 'Rio de Janeiro', 'RJ', 'Maria'),
        ('33344455566', 'Bairro 2', 'Belo Horizonte', 'MG', 'José'),
        ('44455566677', 'Bairro 3', 'Salvador', 'BA', 'Ana'),
        ('55566677788', 'Bairro 4', 'Fortaleza', 'CE', 'Pedro'),
        ('66677788899', 'Centro', 'São Paulo', 'SP', 'Fulano'),
        ('77788899900', 'Bairro 1', 'Rio de Janeiro', 'RJ', 'Beltrano'),
        ('88899900011', 'Bairro 2', 'Belo Horizonte', 'MG', 'Sicrano'),
        ('99900011122', 'Bairro 3', 'Salvador', 'BA', 'Beltrana');""")

    cursor.execute("show tables like 'usuario_web'")
    tables = cursor.fetchone()

    #criando a tabela usuário_web e populando
    if not tables:
        cursor.execute("""CREATE TABLE usuario_web (
        cpf_usuario VARCHAR(11) NOT NULL ,
        nome_login VARCHAR(255) NOT NULL PRIMARY KEY,
        senha VARCHAR(255) NOT NULL,
        FOREIGN KEY (cpf_usuario) REFERENCES usuario (cpf));""")

        data = [
            ("22233344455", "joao@email.com", "senha123"),
            ("33344455566", "maria@email.com", "senha456"),
            ("44455566677", "jose@email.com", "senha789"),
        ]

        for cpf_usuario, nome_login, senha in data:
            cursor.execute("""
            INSERT INTO usuario_web (cpf_usuario, nome_login, senha)
            VALUES (%s, %s, %s)
            """, (cpf_usuario, nome_login, senha))


    cursor.execute("show tables like 'conta'")
    tables = cursor.fetchone()

    #criando a tabela conta e populando
    if not tables:
        cursor.execute("""
        CREATE TABLE conta (
            cpf_usuario VARCHAR(11) NOT NULL,
            id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
            FOREIGN KEY (cpf_usuario) REFERENCES usuario (cpf));""")

        data = [
            ["11122233344"],
            ["22233344455"],
            ["33344455566"],
            ["44455566677"],
            ["55566677788"],
            ["66677788899"],
            ["77788899900"],
            ["88899900011"],
            ["99900011122"],
        ]

        for cpf_usuario in data:
            cursor.execute("""
            INSERT INTO conta (cpf_usuario)
            VALUES (%s)
            """, (cpf_usuario))

    #Aplica as modificações se o bd não existir
    connection.commit()
    return connection