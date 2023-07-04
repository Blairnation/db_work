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
        self.db.read()


    def remove(self):
        row_id = int(input('Enter rowid: ')) 
        self.db.delete(row_id)   


    def get_username(self):
        usernames = self.db.read()
        for username in usernames:
            print(username)

    def start(self):
       while True:
          print('''1.Register\n2.Display\n3.Get Usernames\n3.Delete Info''')
          try: 
           option  = int(input("Enter option: "))
           while option < 1 or option > 4:
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
          except ValueError as err:
              print(f'Error: {err}')

                 

def main():
    # create class Object
    db = InteractDB()
    
    db.start()
if __name__ == '__main__':
    main()