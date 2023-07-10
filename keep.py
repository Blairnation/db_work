import socket
import threading




def handle_client(client_socket):
    while True:  
        msg = client_socket.recv(1024).decode('utf-8')

        if msg is None:
            print('Cilent Disconnected')
            break
        else:
            print(msg)
        send = input('Message: ').encode('utf-8') 
        client_socket.send(send)


def broadcast():
    pass


def start_server():
    client_sockets = []
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = 'localhost'
    port = 5000

    server.bind((host,port))

    server.listen(5)
    print("Server Available. Waiting For Connections...")

    while True:
        client_socket, address = server.accept()
        client_sockets.append(client_sockets) 

        print(f'{address[0]} Connected to server')

        client_thread =  threading.Thread(target=handle_client,args=(client_socket,))
        client_thread.start()



def main():
    
    start_server()  


main()