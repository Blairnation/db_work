import mysql.connector
from mysql.connector import Error

class MySQLDatabase_Crud:
    

    def __init__(self):
        self.host_name = 'Localhost'
        self.user_name = 'root'
        self.password = 'password'
        self.database_name = None
        self.connection = None
        self.cursor = None
        


    
    def create_database(self, database_name):
        try:
            self.connection = mysql.connector.connect(
                host = self.host_name,
                username = self.user_name,
                password = self.password
            )
            self.cursor = self.connection.cursor()

            self.cursor.execute(f'CREATE DATABASE {database_name}')
            self.connection.commit()

            print(f'Database {database_name} Created Successfully')

        except Error as err:
             print(f'Error: {err}')
             


    def drop_database(self, database_name):
        try:
            self.connection = mysql.connector.connect(
                host = self.host_name,
                username = self.user_name,
                password = self.password
            )
            self.cursor = self.connection.cursor()

            self.cursor.execute(f'DROP DATABASE {database_name}')
            self.connection.commit()

            print(f'Database {database_name} Deleted Successfully')

        except Error as err:
             print(f'Error: {err}')            



    def connect_database(self,database_name):
            try:  
                self.database_name = database_name
                self.connection = mysql.connector.connect(
                     host = self.host_name,
                     username = self.user_name,
                     password = self.password,
                     database = self.database_name
                )

                self.cursor = self.connection.cursor()
                print(f'Database {self.database_name} Connected Successfully')
                return self.connection
            
            except Error as err:
                print(f'Error: {err}')



    def show_databases(self):
        try:
            self.connection = mysql.connector.connect(
                host = self.host_name,
                username = self.user_name,
                password = self.password
            )
            self.cursor = self.connection.cursor()

            self.cursor.execute(f'SHOW DATABASES')
            databases = self.cursor.fetchall()
            for database in databases:
                print(database[0])

        except Error as err:
             print(f'Error: {err}')            

  


class MySQLTable_Crud:
    


    def __init__(self,db_name):
      self.conn = MySQLDatabase_Crud().connect_database(db_name) 
      self.cursor = self.conn.cursor()


    def create_table(self): 
        self.cursor.execute(f'''CREATE TABLE IF NOT EXISTS employees
                         (first_name VARCHAR(255),
                          last_name VARCHAR(255) NOT NULL,
                          username VARCHAR(255) NOT NULL PRIMARY KEY,
                          password VARCHAR(255) NOT NULL,
                          age INTEGER CHECK(age>=15),
                          email VARCHAR(255)
                          )''')
        self.conn.commit()
        print('Table Created Successfully')


    def delete_table(self):
        self.cursor.execute('DROP TABLE employees')
        self.conn.commit()
        print('Table Deleted Successfully')


    def insert(self,first_name,last_name,username,password,age,email):
        self.cursor.execute(f'''INSERT INTO employees VALUES{(first_name,last_name,username,password,age,email)}''') 
        self.conn.commit()
        print("Table Insertion Success")  


    def show_employees(self):
        self.cursor.execute('SELECT * FROM employees')
        employees = self.cursor.fetchall()
        for employee in employees:
            print(employee)

        
    def update(self, first_name, last_name, age ,username):
        self.cursor.execute('''UPDATE employees SET first_name = %s, last_name = %s, age = %s
                          WHERE username = %s''', (first_name, last_name, age, username))
        self.conn.commit() 
        print("Table Updated Successfully")   


    def delete(self, email):
        self.cursor.execute('''DELETE FROM employees WHERE email = %s''', (email,))
        self.conn.commit()
        print("Details Deleted Successfully")




def main():
   db = MySQLDatabase_Crud()
   
   # CREATE DATABASE (eg.MobileMoney database)
   # db.create_database("MobileMoney")

   # CONNECT DATABASE
   # db.connect_database()

   # SHOW DATABASES
   #db.show_databases()

   # DROP DATABASE
   # db.drop_database('MobileMoney')

   tb = MySQLTable_Crud('MobileMoney')

   # CREATE TABLE
   # tb.create_table()
   
   # INSERT INTO TABLE
   # tb.insert("Tony", "Blair", 'Blairnation',"blair1", 25, 'tonyblair@gmail.com')
   # tb.insert("Cristiano", "Ronaldo", 'CR7',"cris7", 38, 'christiano@gmail.com')
   # tb.insert("Lionel", "Messi", 'GOAT',"lm10", 36, 'lionelmessi@gmail.com')
   # tb.insert("Kylian", "Mbappe", 'Jon',"turtle", 24, 'kylianmbappe@gmail.com')
   
   # SHOW TABLE
   tb.show_employees()
   
   # UPDATE DETAILS
   # tb.update("Kylian", "Mbappe Lottin", 25, 'Jon')
 
   # DELETE DETAILS
   # tb.delete('kylianmbappe@gmail.com')

   # DELETE TABLE
   # tb.delete_table()

main()        