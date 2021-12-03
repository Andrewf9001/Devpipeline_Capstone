import sqlite3
import bcrypt
from datetime import datetime

class User:
    def __init__(self, user_id, first_name, last_name, phone, email, password, active = 1, date_created, hire_date, user_type = 'User'):
        self.user_id = None
        self.first_name = None
        self.last_name = None
        self.phone = None
        self.email = None
        self.active = None
        self.date_created = None
        self.hire_date = None
        self.user_type = None
        # self.password = 