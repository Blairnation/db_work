import socket
from threading import Thread


# SERVER SIDE CODE
class Server:
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = 'localhost'
        self.port = 5000
        self.clients_list = []

    def start(self):
        self.server.bind((self.host, self.port))
        self.server.listen(5)
        print('Server Active. Waiting for connections..')
        while True:
            client_socket, address = self.server.accept()
            print(f'{address} Connected to Server')
            self.clients_list.append(client_socket)

            socket_thread = Thread(target=self.handle_client, args=(client_socket,))
            socket_thread.start()

    def handle_client(self, client_socket):
        while True:
            msg = client_socket.recv(1024).decode('utf-8')
            if msg == '':
                print("Client Disconnected")
                self.clients_list.remove(client_socket)
                break
            else:
                self.broadcast_msg(client_socket, msg.encode('utf-8'))

    def broadcast_msg(self, sender_socket, msg):
        for client_socket in self.clients_list:
            if client_socket != sender_socket:
                client_socket.send(msg)

# server = Server()  
# server.start()




# CLIENT SIDE CODE (Can be two or more)

import socket
from threading import Thread

class Client:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = 'localhost'
        self.port = 5000


    def start(self):
        self.client.connect((self.host, self.port))

        recieve_thread = Thread(target=self.recieve_msg)
        recieve_thread.start()

        while True:
            send_msg = input('> ').encode('utf-8')
            self.client.send(send_msg)
            if send_msg.decode('utf-8') == '':
                print('Server Disconnected')
                break


    def recieve_msg(self):
        while True:
            msg = self.client.recv(1024).decode('utf-8')
            if msg == '':
                print('Server Disconnected')
                break
            else:
                print(msg)  

                
# client = Client()
# client.start()
