import sqlite3

con = sqlite3.connect('data.db')
con.execute('''
    CREATE TABLE url (id INTEGER PRIMARY KEY, url char(200) 
    NOT NULL, shortId char(20) NOT NULL)
    ''')
con.commit()
