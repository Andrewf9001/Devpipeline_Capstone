import sqlite3
import bcrypt
from datetime import datetime

class Users:
    def __init__(self):
        self.user_id = None
        self.first_name = None
        self.last_name = None
        self.phone = None
        self.email = None
        self.active = None
        self.date_created = None
        self.hire_date = None
        self.user_type = None
        self.__password = None


    def set_all(self, first_name, last_name, phone, email, password, date_created, user_type = "User", hire_date = None):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.date_created = date_created
        self.user_type = user_type
        self.hire_date = hire_date
        self.__password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


    def get_date(self):
        new_date = datetime.now()
        date_time_str = new_date.strftime("%Y-%m-%d %H:%M:%S")
        return date_time_str


    def change_password(self, new_password):
        if new_password:
            self.__password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())

    
    def check_password(self, email, new_password, cursor):
        data = cursor.execute("SELECT email, password FROM Users")

        for row in data:
            continue

        hashed_password = row[1]

        valid_password = bcrypt.hashpw(new_password.encode('utf-8'), hashed_password)

        if valid_password == hashed_password:
            select_sql = '''
                SELECT email FROM Users WHERE password = ? AND email = ?;
            '''

            row = cursor.execute(select_sql, (valid_password, email)).fetchone()

            return (row != None)
        # else:
        #     print("\nIncorrect Password\n")


    def change_email(self, new_email):
        self.email = new_email


    def save_user(self, cursor):
        insert_sql = '''
            INSERT INTO Users
                (first_name, last_name, phone, email, password, date_created, user_type, hire_date)
            VALUES
                (?, ?, ?, ?, ?, ?, ?, ?);
        '''

        cursor.execute(insert_sql, (self.first_name, self.last_name, self.phone, self.email, self.__password, self.date_created, self.user_type, self.hire_date))
        cursor.connection.commit()

        new_user_id = cursor.execute('SELECT last_insert_rowid()').fetchone()
        self.user_id = new_user_id[0]


    def print_me(self):
        print(f'{self.user_id} {self.last_name}, {self.first_name}')
        print(f'  {self.email}')
        print(f'  Created: {self.date_created}')


    def load(self, cursor):
        select_sql = '''
            SELECT user_id, first_name, last_name, phone, email, date_created, hire_date, user_type
            FROM Users
            WHERE user_id = ?;
        '''

        row = cursor.execute(select_sql, (self.user_id, )).fetchone()

        if not row:
            print("No Results")
            return
        self.user_id = row[0]
        self.first_name = row[1]
        self.last_name = row[2]
        self.phone = row[3]
        self.email = row[4]
        self.date_created = row[5]
        self.hire_date = row[6]
        self.user_type = row[7]


class User(Users):
    def change_name(self, new_first, new_last, id, cursor):
        update_sql = '''
            UPDATE Users
            SET first_name = ?, last_name = ?
            WHERE user_id = ?
        '''

        cursor.execute(update_sql, (new_first, new_last, id))
        connection.commit()

    # def change_email(self, new_email, id, cursor):
    #     update_sql = '''
    #         UPDATE Users
    #         SET email = ?
    #         WHERE user_id = ?
    #     '''

    #     cursor.execute(update_sql, (new_email, id))
    #     connection.commit()

    # def change_password(self, cursor):
    #     update_sql = '''
    #         UPDATE Users
    #         SET password = ?
    #         WHERE user_id = ?
    #     '''

    #     cursor.execute(update_sql, (new_email, id))
    #     connection.commit()


    def view_compentency_list(self, cursor):
        select_sql = '''
            SELECT * FROM AssessmentResults WHERE user_id = ?
        '''
        rows = cursor.execute(select_sql, (self.user_id, ))

        # for row in rows:
        #     if row == None:
        #         print("No compentency assessments yet")
        #     else:
        #         print("List of shit")


    # change email and change password inherited

class Manager(Users):
    pass

connection = sqlite3.connect('compentancy.db')
cursor = connection.cursor()

# new_user = Users()
# name_change = User()

# new_user.set_all("Andrew", "Fletcher", "8019349230", "af@test.com", "123", new_user.get_date(), "Manager", new_user.get_date())
# new_user.save_user(cursor)
# new_user.load(cursor)
# new_user.print_me()

# name_change.set_all("Test", "Namechange", "8024039342", "test@test.com", "test", new_user.get_date())
# name_change.change_name('Josh', 'Dielmann', 3, cursor)
# name_change.change_email("jd@test.com", 3, cursor)
# name_change.load(cursor)
# print(name_change.view_compentency_list(cursor))
# name_change.save_user(cursor)
# name_change.load(cursor)
# name_change.print_me()



# new_user.set_all("Adam", "Armstrong", "2349280958", "aj@test.com", "234", new_user.get_date())
# new_user.save_user(cursor)
# new_user.load(cursor)
# new_user.print_me()

# print(new_user.check_password(new_user.email, "123", cursor))
# new_user.change_password("1234")
# print(new_user.check_password("af@test.com", "1234", cursor))