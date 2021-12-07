import sqlite3
from Users import Users #, User, Manager
import initialization as initial
import getpass

connection = sqlite3.connect('compentancy.db')
cursor = connection.cursor()


def login(cursor):
    login = Users()
    email_input = input("Enter Email: ")
    # password_input = input("Enter Password: ")
    password_input = getpass.getpass('Enter Password: ')


    if '@' not in email_input and '.' not in email_input:
        print("\nWrong Email\n")
    else:
        check_pw = login.check_password(email_input, password_input, cursor)
        if not check_pw:
            print("\nWrong Password\n")
        else:
            return check_pw

def type_of_user(cursor):
    pass