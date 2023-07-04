from sqlitedb import SQliteDatabase

class InteractDB:
    
    def __init__(self):
        self.db = SQliteDatabase()
        self.connect = self.db.connect_database()
        self.db.create_table()


    def register(self):
        user_name = input('Username: ')
        email = input('email: ')
        address = input('Address: ')
        password = input('password: ')
        self.db.insert((user_name, email, address,password))


    def display_database(self):
        emp_data = self.db.read()
        for data in emp_data:
            print(data)


    def remove(self):
        row_id = int(input('Enter rowid: ')) 
        self.db.delete(row_id)   


    def get_username(self):
        user_names = self.db.read()
        for emp in user_names:
            print(emp[1])


    def update_info(self):
        email = input('Enter Email: ')
        password = input('Enter password: ')
        username = input('Enter new username: ')
        address = input('Enter new address: ')
        self.db.update(email, password, username, address)        

    def start(self):
       while True:
          print('''1.Register\n2.Display\n3.Get Usernames\n4.Delete Info\n5.Update''')
          try: 
            option  = int(input("Enter option: "))
            while option < 1 or option > 5:
                option = int(input('Enter valid option: '))    
            if option == 1:
                self.register()
                print('Registered Succesfully')
                break
            elif option == 2:
                    self.display_database()
                    break
            elif option == 3:
                    self.get_username()
                    break
            elif option == 4:
                self.remove()
                break
            elif option == 5:
                self.update_info()
                break
          except ValueError as err:
              print(f'Error: {err}')

                 

def main():
    # create class Object
    db = InteractDB()
    
    db.start()
if __name__ == '__main__':
    main()