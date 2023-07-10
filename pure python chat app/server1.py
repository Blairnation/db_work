import sqlite3
import socket
from threading import Thread



class Server:
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = 'localhost'
        self.port = 5000
        self.clients_list = []


    def start(self):
        self.server.bind((self.host, self.port))  
        self.server.listen(5)
        print("Server Active. Waiting for connections...")

        while True:
            client_socket, address = self.server.accept()
            print(f'{address} Connected To Server')
            self.clients_list.append(client_socket)

            self.client_thread = Thread(target=self.handle_client, args=(client_socket, ))
            self.client_thread.start()


    def handle_client(self, client_socket):
        while True:
            recieve_msg = client_socket.recv(1024).decode('utf-8')
            if recieve_msg == '':
                self.clients_list.remove(client_socket)
                print('Client Disconnected')
                if self.clients_list == []:
                   break
            else:
                self.send_msg(recieve_msg, client_socket)


    def send_msg(self, msg, sender_socket):
        for clients in self.clients_list:
            if clients != sender_socket:
                clients.send(msg.encode('utf-8'))


server = Server() 
server.start()               


