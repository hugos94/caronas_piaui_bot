import sqlite3

def connect():
    global conn, cursor

    conn = sqlite3.connect('caronas.db')
    cursor = conn.cursor()

    print('Conexao criada!')

def disconnect():
    global conn
    conn.close()

    print('Conexao finalizada!')

def create_table():
    global cursor
    cursor.execute("""
        CREATE TABLE caronas (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER,
            cpf     VARCHAR(11) NOT NULL,
            contato TEXT,
            cidade_from TEXT,
            cidade_to TEXT,
            criado_em DATE NOT NULL
    );
    """)
    print('Tabela criada com sucesso.')

def insert_ride():
    pass

def remove_ride():
    pass

def update_ride():
    pass

def search_ride():
    pass

def list_rides():
    pass
