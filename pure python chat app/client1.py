import sqlite3
import socket
from threading import Thread



class Client:
    
    def __init__(self, num):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = 'localhost'
        self.port = 5000
        self.num = num

    def start(self):
           self.client.connect((self.host, self.port))

           self.recieve_msg_thread = Thread(target=self.recieve_msg)
           self.recieve_msg_thread.start()

           print('CHAT CONSOLE')
           print('==============')
           while True:
                send_msg = input(' ').encode('utf-8')
                self.client.send(send_msg)
                print('Message Sent')
                if send_msg.decode('utf-8') == '':
                     print('Disconnected From Server')
                     break



    def recieve_msg(self):
         while True:
            recieve_msg = self.client.recv(1024).decode('utf-8')
            if recieve_msg == '': 
                 print(f'{self.num} Offline')
                 break
            else:
                 print()
                 print(recieve_msg) 
                 print(f"Message Recieved From {self.num}") 


# client = Client()
# client.start()
