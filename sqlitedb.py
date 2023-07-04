import sqlite3

from sqlite3 import Error

class SQliteDatabase:
    
    def __init__(self):
        self.connection = None
        self.cursor = None


    def connect_database(self):
        self.connection = sqlite3.connect('Company.db')
        self.cursor = self.connection.cursor()
 

    def create_table(self):
        self.cursor = self.connection.cursor()
        self.cursor.execute(f'''CREATE TABLE IF NOT EXISTS employees 
                             (user_name TEXT,
                             email TEXT UNIQUE,
                             address TEXT,
                             password TEXT
                             )'''
                                       )
        self.connection.commit()



    def insert(self,details):
        self.cursor.execute('INSERT INTO employees(user_name,email,address,password) VALUES(?,?,?,?)', details)
        self.connection.commit()



    def read(self):
        self.cursor.execute('SELECT rowid,* FROM employees')
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)
       


    def delete(self,id):
        self.cursor.execute(f'''DELETE FROM employees WHERE rowid = {id}''')
        self.connection.commit()



    def update(self,new_email, password, address):
        self.cursor.execute(f'''UPDATE employees SET address = {address},
                                email = {new_email}
                                WHERE password = {password}''')
        


# db =SQliteDatabase()