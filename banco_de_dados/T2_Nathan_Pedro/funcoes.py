import PySimpleGUI as sg

def janela_login():
    sg.theme('Reddit')
    layout_login = [
        [sg.Text("Meu Banco de Dados", size=(20, 1), font=('Arial', 25), justification='center', pad=((0, 0), (30, 20)))],
        [sg.Button("Login como Usuário", size=(30, 2), button_color=("white", "#6495ED"), key="usuario", pad=((50, 50), (10, 10)))],
        [sg.Button("Login como Atendente", size=(30, 2), button_color=("white", "#6495ED"), key="atendente", pad=((50, 50), (10, 10)))],
        [sg.Button("Sair", size=(10, 1), button_color=("white", "red"), key="sair", pad=((10, 0), (20, 10)))]
    ]
    return sg.Window("Login", layout_login, background_color="white", element_justification='c')


def janela_login_usuario():
    sg.theme('Reddit')
    layout_login_usuario = [
        [sg.Text('Login', font=('Helvetica',20), text_color='blue', justification='center' ,size=(10, 2),background_color='white')],
        [sg.Input(default_text="Nome", size=(30, 10), justification="center"), sg.Input("Senha", size=(20,10), justification="center")],
        [sg.Button("Login", font="Arial 16", button_color="blue", size=(5, 2))]
    ]
    return sg.Window("Login de usuario",layout_login_usuario)

def janela_login_atendente():
    sg.theme('Reddit')
    layout_login_atendente = [
        [sg.Text('Outro texto',size = (40,10), font = ('Arial',40))]
    ]
    janela = sg.Window("Tela 1",layout_login_atendente)
    return None