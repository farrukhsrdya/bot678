import sqlite3



connection = sqlite3.connect('delivery.db', check_same_thread=False)

sql = connection.cursor()



sql.execute('CREATE TABLE IF NOT EXISTS users(id INTEGER, name TEXT, number TEXT UNIQUE);')




def register(tg_id, name, num):
    sql.execute('INSERT INTO users VALUES (?, ?, ?);', (tg_id, name, num))

    connection.commit()

def check_user(tg_id):
    if sql.execute('SELECT * FROM users WHERE id=?;', (tg_id,)).fetchone():
        return True
    else:
        return False


