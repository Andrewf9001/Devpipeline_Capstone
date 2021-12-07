# from os.path import exists
# from users import *
import sqlite3
import initialization
import functionality as func

connection = sqlite3.connect('compentancy.db')
cursor = connection.cursor()

print("""
    Hello, Fred Ward, you are our first Manager
    Below is your login credentials
    Email: fredward1@gmail.com
    Password: fw123

    Please Login so we can begin!
""")

def main(cursor):
    loggin_in = func.login(cursor)

    if not loggin_in:
        # print("\nSorry something went wrong, please try again\n")
        main(cursor)
    else:
        print("Welcome")


# print(comp_query(cursor))
main(cursor)
