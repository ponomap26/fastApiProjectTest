import sqlite3

def create_db(db_file):

    # Создаем соединение с базой данных
    conn = sqlite3.connect(db_file)

    # Создаем курсор
    c = conn.cursor()

    # Проверяем, существует ли таблица 'user'
    c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='user'")
    table = c.fetchone()

    # Если таблица 'user' не существует, создаем ее
    if table is None:
        c.execute('''CREATE TABLE user
                     (id integer PRIMARY KEY, name text, email text, password text, status integer)''')

    # Проверяем, существует ли таблица 'product'
    c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='product'")
    table = c.fetchone()

    # Если таблица 'product' не существует, создаем ее
    if table is None:
        c.execute('''CREATE TABLE product
                     (id integer PRIMARY KEY, name text, price real, description text, image text)''')

    # Сохраняем изменения
    conn.commit()

    # Закрываем соединение
    conn.close()
    print('Соединение с базой данных установлено')
    return


create_db('my_database.db')




