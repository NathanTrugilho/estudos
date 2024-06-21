import mysql.connector

def criabanco():

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
    cursor.execute("use loja")

    cursor.execute("show tables like 'usuario'")
    tables = cursor.fetchone()
    if not tables:
        # Criar a tabela
        cursor.execute("""
            CREATE TABLE usuario(
                cpf CHAR(11) PRIMARY KEY,
                nome VARCHAR(40) NOT NULL,
                bairro VARCHAR(40) NOT NULL,
                cidade VARCHAR(40) NOT NULL,
                estado VARCHAR(2) NOT NULL)
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
        ('99900011122', 'Bairro 3', 'Salvador', 'BA', 'Beltrana')""")

    cursor.execute("show tables like 'usuario_web'")
    tables = cursor.fetchone()
    #criando a tabela usuário_web e populando
    if not tables:
        cursor.execute("""CREATE TABLE usuario_web (
        cpf_usuario VARCHAR(11) NOT NULL,
        nome_login VARCHAR(30) NOT NULL,
        senha  VARCHAR(60) NOT NULL NOT NULL,
        PRIMARY KEY (cpf_usuario, nome_login),
        FOREIGN KEY (cpf_usuario) REFERENCES usuario(cpf))""")

        data = [
            ("22233344455", "joao@email.com", "senha123"),
            ("33344455566", "maria@email.com", "senha456"),
            ("44455566677", "jose@email.com", "senha789"),
        ]

        for cpf_usuario, nome_login, senha in data:
            cursor.execute("""INSERT INTO usuario_web (cpf_usuario, nome_login, senha)
            VALUES (%s, %s, %s)
            """, (cpf_usuario, nome_login, senha))


    #criando a tabela conta e populando ======================
    cursor.execute("show tables like 'conta'")
    tables = cursor.fetchone()
    if not tables:
        cursor.execute("""
        CREATE TABLE conta (
            id INT AUTO_INCREMENT PRIMARY KEY,
            cpf_usuario VARCHAR(11) NOT NULL,
            FOREIGN KEY (cpf_usuario) REFERENCES usuario (cpf))""")

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

    #tabela pedido ========================================
    cursor.execute("show tables like 'pedido'")
    tables = cursor.fetchone()
    if not tables:
        cursor.execute("""
        CREATE TABLE pedido (
            id INT AUTO_INCREMENT PRIMARY KEY,
            status VARCHAR(20) NOT NULL,
            data DATE NOT NULL,        
            id_conta INT NOT NULL,
            cpf_atendente VARCHAR(11) NULL, 
            FOREIGN KEY (id_conta) REFERENCES conta(id)
        )
    """) #se o cpf_atendente for null então o pedido foi feito pela web
        data = [
            ( 'Pendente', '2023-01-15', 1, '98765432109'),
            ( 'Concluído', '2023-01-16', 2, 'NULL'),
            ( 'Pendente', '2023-01-17', 3, '11223344556'),
            ( 'Concluído', '2023-01-18', 4, 'NULL'),
            ( 'Pendente', '2023-01-19', 5, '44556677889'),
            ( 'Pendente', '2024-01-19', 6, '44556677889'),
        ]

        for status, data_pedido, id_conta, cpf_atendente in data:
            cursor.execute("""
            INSERT INTO pedido (status, data, id_conta, cpf_atendente)
            VALUES ( %s, %s, %s, %s)
            """, ( status, data_pedido, id_conta, cpf_atendente))

    #tabela pagamento =========================================
    cursor.execute("show tables like 'pagamento'")
    tables = cursor.fetchone()
    if not tables:
        cursor.execute("""
        CREATE TABLE pagamento (
            id INT AUTO_INCREMENT,
            id_pedido INT,
            parcela INT,
            forma_pagamento VARCHAR(30) NOT NULL,
            valor DECIMAL(8,2) NOT NULL,
            PRIMARY KEY (id, id_pedido, parcela),
            FOREIGN KEY (id_pedido) REFERENCES pedido(id)
        )
    """)
        data = [
            ( '6', '1', 1, '10'),
        ]

        for id_pedido, parcela, forma_pagamento, valor in data:
            cursor.execute("""
            INSERT INTO pagamento (id_pedido, parcela, forma_pagamento, valor)
            VALUES ( %s, %s, %s, %s)
            """, ( id_pedido, parcela, forma_pagamento, valor))
    
    #tabela produto ==============================================
    cursor.execute("show tables like 'produto'")
    tables = cursor.fetchone()
    if not tables:
        cursor.execute("""
        CREATE TABLE produto (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(50),
            valor DECIMAL(8,2)
        )
    """)
        # MUDEI OS PREÇOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOS
        data = [
        ("camiseta","30"),
        ("camisa","40"),
        ("casaco","75"),
        ("cropped","15"),
        ("calça","60"),
        ("bermuda","50"),
        ("saia","120"),
        ("tênis","300"),
        ("sapato","380"),
        ("sapatilha","200"),
        ]

        # MUDEI PRA INSERIR O PREÇOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
        for nome, valor in data:
            cursor.execute(""" INSERT INTO produto(nome, valor) VALUES (%s, %s)""", (nome, valor))
        #Aplica as modificações se o bd não existir
        connection.commit()

    #tabela item ================================================
    cursor.execute("show tables like 'item'")
    tables = cursor.fetchone()
    if not tables:
        cursor.execute("""
        CREATE TABLE item (
            id INT AUTO_INCREMENT PRIMARY KEY,
            id_produto INT,
            nome VARCHAR(50),
            quantidade INT NOT NULL,
            FOREIGN KEY (id_produto) REFERENCES produto(id)
        )
    """)
        data = [
        ("1","camiseta vermelha", "100"),
        ("1","camiseta verde", "100"),
        ("1","camiseta preta", "100"),
        ("1","camiseta azul", "100"),
        ("1","camiseta branca", "100"),
        ("2","camisa social preta", "100"),
        ("2","camisa social branca", "100"),
        ("2","camisa regata branca", "100"),
        ("2","camisa regata estampada", "100"),
        ("2","camisa polo preta", "100"),
        ("3","casaco vermelho", "100"),
        ("3","casaco branco", "100"),
        ("3","casaco preto", "100"),
        ("3","casaco verde", "100"),
        ("4","cropped vermelho", "100"),
        ("4","cropped branco", "100"),
        ("4","cropped preto", "100"),
        ("4","cropped verde", "100"),
        ("5","calça vermelha", "100"),
        ("5","calça branca", "100"),
        ("5","calça preta", "100"),
        ("5","calça verde", "100"),
        ("6","bermuda vermelha", "100"),
        ("6","bermuda branca", "100"),
        ("6","bermuda preta", "100"),
        ("6","bermuda verde", "100"),
        ("7","saia vermelha", "100"),
        ("7","saia branca", "100"),
        ("7","saia preta", "100"),
        ("7","saia verde", "100"),
        ("8","tênis vermelho", "100"),
        ("8","tênis branco", "100"),
        ("8","tênis preto", "100"),
        ("8","tênis verde", "100"),
        ("9","sapato vermelho", "100"),
        ("9","sapato branco", "100"),
        ("9","sapato preto", "100"),
        ("9","sapato verde", "100"),
        ("10","sapatilha vermelha", "100"),
        ("10","sapatilha branca", "100"),
        ("10","sapatilha preta", "100"),
        ("10","sapatilha verde", "100"),
        
        ]

        for id_produto, nome, quantidade in data:
            cursor.execute(""" INSERT INTO item(id_produto, nome, quantidade) VALUES (%s, %s, %s)""", (id_produto, nome, quantidade))
        #Aplica as modificações se o bd não existir
        connection.commit()

    #tabela carrinho de compras ===================================
    cursor.execute("show tables like 'carrinho_de_compras'")
    tables = cursor.fetchone()
    if not tables:
        cursor.execute("""
        CREATE TABLE carrinho_de_compras (
            id INT AUTO_INCREMENT,
            id_conta INT, 
            PRIMARY KEY (id, id_conta),
            FOREIGN KEY (id_conta) REFERENCES conta(id)
        )
    """)
    
    #tabela de relação entre item e carrinho de compras ============
    cursor.execute("show tables like 'relacao_carrinho_item'")
    tables = cursor.fetchone()
    if not tables:
        cursor.execute("""
        CREATE TABLE relacao_carrinho_item (
            id_carrinho_de_compras INT,
            id_conta_carrinho_de_compras INT, 
            id_item INT,
            quantidade INT,
            valor DECIMAL(8,2),
            nome VARCHAR(30),
            PRIMARY KEY (id_carrinho_de_compras, id_conta_carrinho_de_compras, id_item),
            FOREIGN KEY (id_conta_carrinho_de_compras) REFERENCES carrinho_de_compras(id_conta),
            FOREIGN KEY (id_carrinho_de_compras) REFERENCES carrinho_de_compras(id),
            FOREIGN KEY (id_item) REFERENCES item(id)
            )
    """)
        
    
    #tabela de relação entre item e pedido ===========================
    cursor.execute("show tables like 'relacao_item_pedido'")
    tables = cursor.fetchone()
    if not tables:
        cursor.execute("""
        CREATE TABLE relacao_item_pedido (
            id_pedido INT,
            id_item INT,
            quantidade_item INT,
            PRIMARY KEY (id_pedido, id_item),
            FOREIGN KEY (id_pedido) REFERENCES pedido(id),
            FOREIGN KEY (id_item) REFERENCES item(id)
            )
    """)
    
    cursor.execute("show tables like 'atendente'")
    tables = cursor.fetchone()
    #criando a tabela atendente e populando
    if not tables:

        cursor.execute("""
        CREATE TABLE atendente (
            cpf CHAR(11),
            nome_login VARCHAR(40) NOT NULL, 
            senha VARCHAR(60) NOT NULL,
            PRIMARY KEY (CPF)
        )
    """)
        data = [
        ("12345678901", "joaoqlqr@gmail.com", "12345678"),
        ("98765432109", "mariaqlqr@gmail.com", "23456744"),
        ("11223344556", "carlosqlqr@gmail.com", "34567844"),
        ("44556677889", "anaqlqr@gmail.com", "45678944"),
        ("55667788990", "José Pereira", "56789044"),
        ("66778899001", "Clara Machado", "67890144"),
        ("77889900112", "Luiz Silva", "78901244"),
        ("88990011223", "Fernanda Costa", "89012344"),
        ("99001122334", "Carlos Santos", "90123444"),
        ]

        for cpf, nome, senha in data:
            cursor.execute("""
            INSERT INTO atendente (CPF, nome_login, senha)
            VALUES (%s, %s, %s)
            """, (cpf, nome, senha))
    #Aplica as modificações se o bd não existir
    connection.commit()
    return None

criabanco()