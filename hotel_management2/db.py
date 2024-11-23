import sqlite3

def create_connection():
    """Создание подключения к базе данных SQLite."""
    conn = sqlite3.connect('hotel_clients.db')
    return conn

def create_table():
    """Создание таблицы для клиентов, если она не существует."""
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS clients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        patronymic TEXT,
        birth_date TEXT,
        check_in_date TEXT,
        check_out_date TEXT
    );
    ''')
    conn.commit()
    conn.close()

def add_client(first_name, last_name, patronymic, birth_date, check_in_date, check_out_date):
    """Добавление нового клиента в базу данных."""
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO clients (first_name, last_name, patronymic, birth_date, check_in_date, check_out_date)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (first_name, last_name, patronymic, birth_date, check_in_date, check_out_date))
    conn.commit()
    conn.close()

def get_all_clients():
    """Получение списка всех клиентов."""
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clients')
    clients = cursor.fetchall()
    conn.close()
    return clients
