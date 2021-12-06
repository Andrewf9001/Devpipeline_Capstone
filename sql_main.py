import sqlite3
from datetime import datetime

def create_tables(cursor):

  with open('sql_tables.sql') as sql_file:
    sql_as_string = sql_file.read()
    cursor.executescript(sql_as_string)

  connection.commit()

def insert_compentencies(cursor):
  new_date = datetime.now()
  date_time_str = new_date.strftime("%Y-%m-%d %H:%M:%S")
  comp_list = [
    "Data Types",
    "Variables",
    "Functions",
    "Boolean Logic",
    "Conditionals",
    "Loops",
    "Data Structures",
    "Lists",
    "Dictionaries",
    "Working with Files",
    "Exception Handling",
    "Quality Assurance (QA)",
    "Object-Oriented Programming",
    "Recursion",
    "Databases"
  ]

  for item in comp_list:
    insert_sql = '''
      INSERT INTO Compentencies
        (name, date_created)
      VALUES 
        (?, ?)
    ;'''

    cursor.execute(insert_sql, (item, date_time_str))
    cursor.connection.commit()
  
  

connection = sqlite3.connect('compentancy.db')
cursor = connection.cursor()

create_tables(cursor)
insert_compentencies(cursor)