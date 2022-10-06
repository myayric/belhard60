import sqlite3

conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    name VARCHAR(20) NOT NULL,
    email VARCHAR(20) NOT NULL UNIQUE
);
''')
conn.commit()


cur.execute('''
CREATE TABLE IF NOT EXISTS post (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    title VARCHAR(20) NOT NULL,
    body VARCHAR(140) NOT NULL UNIQUE,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);
''')
conn.commit()

# cur.execute('''
# AFTER TABLE posts ADD is_published BOOLEAN DEFAULT(false);
# ''')
# conn.commit()

# cur.execute('''
# INSERT INTO users(name, email) VALUES(?, ?);
# ''', ('mohsen', 'info@infdo.com'))
# conn.commit()
#
# cur.execute('''
# UPDATE user SET name=? WHERE id=?;
# ''', ('pasha', 1))
# conn.commit()

# cur.execute('''
# DELETE FROM users WHERE id=?;
# ''', (1, ))
# conn.commit()

# cur.execute('''
# SELECT * FROM users;
# ''')
# for user in cur.fetchall():
#     print(user)


# cur.execute('''
# SELECT * FROM users JOIN post ON users.id = post.user_id;
# ''')
# for user in cur.fetchall():
#     print(user)
