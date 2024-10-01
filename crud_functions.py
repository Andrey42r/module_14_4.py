import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()


def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    );
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price TEXT NOT NULL
    );
    ''')


for i in range(4):
    cursor.execute("INSERT INTO Products(title, description, price) VALUES (?, ?, ?)",
                   (f"Product{i + 1}", f"Описание{i + 1}", f"{(i + 1) * 100}"))
    cursor.execute("DELETE FROM Users")


def add_user(username, email, age):
    cursor.execute(f"INSERT INTO Users(username, email, age, balance) VALUES ('{username}', '{email}', '{age}', 1000)")
    connection.commit()


def is_included(username):
    user = cursor.execute('SELECT * FROM Users WHERE username = ?', (username,))
    if user.fetchone() is None:
        return True
    else:
        return False


def get_all_products():
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()
    connection.commit()
    connection.close()
    return products


def add_product(title, description, price):
    initiate_db()
    conn = sqlite3.connect('products.db')
    c = conn.cursor()
    c.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)", (title, description, price))
    conn.commit()
    conn.close()


add_product('Product1', '1', 100)
add_product('Product2', '2', 200)
add_product('Product3', '3', 300)
add_product('Product4', '4', 400)
