import sqlite3
from client1 import Client


class DB:
     
     def __init__(self):
          self.conn = sqlite3.connect('store.db')
          self.cur = self.conn.cursor()


     def display(self):
          self.cur.execute('SELECT * FROM persons')
          persons = self.cur.fetchall()
          print()
          print('Contacts')
          for person in persons:
               print(f'{person[0]} \t {person[1]}')
                       


     def save(self,name, phone):
          self.cur.execute('INSERT INTO persons VALUES(?,?)',(name, phone))
          self.conn.commit() 
          print(f'{name} Saved To Contacts') 


     def delete(self, phone):
          self.cur.execute('DELETE FROM persons WHERE phone_number = ?',(phone,))
          self.conn.commit()
          print(f'{phone} Deleted From Contacts')


     def edit(self, name, phone):
          self.cur.execute('UPDATE persons SET person = ? WHERE phone_number = ?',(name, phone))
          self.conn.commit()
          print('Contact Details Updated')


     def menu(self):
         while True:
            print()
            print('1.Chat\n2.Add Contact\n3.Delete Contact\n4.Edit Contact')
            option = int(input('Select Option: '))
            if option == 1:
                self.chat()
            elif option == 2:
                name = input('Enter name: ')
                num = input('Enter num: ')
                self.save(name, num)
            elif option == 3:
                num = input('Enter Number: ')
                self.delete(num)
            elif option == 4:
                name = input('Enter New Name: ')
                num = input('Enter Number: ')
                self.edit(name,num)
            else:
                break     
         
             

     def chat(self):
         while True:
            self.display()
            phone_num = input("Enter Phone Number: ")
            self.cur.execute('SELECT * FROM persons WHERE phone_number = ?', (phone_num,))
            exists = self.cur.fetchall()
            if exists:
                for name in exists:
                     name = name[0]
                     client = Client(name)
                     client.start()
                break
            if not exists:
                print('Number Not Available')
                return 
            
         

db = DB() 
db.menu()

