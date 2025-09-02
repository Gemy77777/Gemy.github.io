import sqlite3
try:
    db = sqlite3.connect('Test.db')
    print("Database opened successfully.")
    cr = db.cursor()
    cr.execute('CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY, name TEXT)')
    my_list = ['Gamal', 'Ahmed', 'Sara']
    # for user in my_list:
    #     cr.execute(f'INSERT INTO users (name) VALUES ("{user}")')
    # db.commit()
    cr.execute('SELECT * FROM users')
    rows = cr.fetchall()
    print("Data retrieved successfully.")
    print(f'Number of rows: {len(rows)}')
    print('Users:')
    for row in rows:
        print(f'User ID: {row[0]}, Name: {row[1]}')
    print("All users retrieved successfully.")
except sqlite3.Error as e:
    print("An error occurred:", e)
finally:
    if db:
        db.close()
