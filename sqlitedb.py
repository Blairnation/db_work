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
        return rows
       


    def delete(self,id):
        self.cursor.execute(f'''DELETE FROM employees WHERE rowid = {id}''')
        print("Detail Deleted Successfully")
        self.connection.commit()



    def update(self,email, password,username, address):
        self.cursor.execute('''SELECT * FROM employees WHERE email == ? 
                                         AND password == ?''', (email,password))
        
        exist = self.cursor.fetchone()
        if exist:
            self.cursor.execute('''UPDATE employees SET user_name = ?,
                                    address = ? 
                                    WHERE email = ? AND password = ?''',
                                    (username,address,email,password))
            self.connection.commit()
            print('Updated Successfully')
            
        else:
            print('Invalid Email OR Password!!')
            
        


# db =SQliteDatabase()