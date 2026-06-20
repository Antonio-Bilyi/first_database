import sqlite3

def create_db():

    with open('tables.sql', 'r') as file:

        sql = file.read()
    
    with sqlite3.connect('tables.db') as connection:
        
        current = connection.cursor()

        current.executescript(sql)


if __name__ == '__main__':

    create_db()