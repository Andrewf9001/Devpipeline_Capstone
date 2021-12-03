import sqlite3

def create_tables(cursor):

  with open('sql_tables.sql') as sql_file:
    sql_as_string = sql_file.read()
    cursor.executescript(sql_as_string)

  connection.commit()

connection = sqlite3.connect('compentancy.db')
cursor = connection.cursor()

create_tables(cursor)