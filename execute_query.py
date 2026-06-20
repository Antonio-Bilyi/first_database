import sqlite3

def execute_query(filepath: str) -> list:

    with open(filepath, 'r', encoding='utf-8') as file:

        sql = file.read()
    
    with sqlite3.connect('tables.db') as connection:

        current = connection.cursor()
        current.execute(sql)

        return current.fetchall()

for i in range(1, 13):

    filename = f'query_{i}.sql'
    print(f'---{filename}---')
    print(execute_query(filename))