import sqlite3
from datetime import datetime

from Users import Users

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


def compentency_query(cursor):
    select_sql = '''
        SELECT count(name) FROM Compentencies;
    '''

    count = cursor.execute(select_sql)

    for row in count:
        if row[0] == 0:
            insert_compentencies(cursor)


def new_manager(cursor):
  new_manager = Users()
  select_sql = '''
      SELECT count(user_id) FROM Users;
  '''

  count = cursor.execute(select_sql)

  for row in count:
      if row[0] == 0:
          new_manager.set_all("Fred", "Ward", "3982931039", "fredward1@gmail.com", "fw123", new_manager.get_date(), "Manager", new_manager.get_date())
          new_manager.save_user(cursor)


connection = sqlite3.connect('compentancy.db')
cursor = connection.cursor()

create_tables(cursor)
compentency_query(cursor)
new_manager(cursor)