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
        CREATE TABLE rides (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            username TEXT NOT NULL,
            spots INTEGER NOT NULL,
            contribution INTEGER NOT NULL,
            #cpf VARCHAR(11) NOT NULL,
            contact TEXT,
            from_city TEXT,
            to_city TEXT,
            ride_date DATE NOT NULL,
            created_in DATE NOT NULL
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
