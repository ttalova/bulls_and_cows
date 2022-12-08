import os
import socket
import threading

host = '127.0.0.1'
port = 5096

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(2)

clients = []
numbers = []
main_num = {}


def broadcast(message, client):
    for client_1 in clients:
        if client == client_1:
            client_1.send(message)


def handle(client):
    while True:
        try:
            message = client.recv(1024)
            for client_1 in clients:
                if client_1 != client:
                    message += f'{main_num[client_1]}'.encode('ascii')
            broadcast(message, client)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            client = clients[index]
            clients.remove(client)
            break


def receive():
    while len(clients)<2:
        client, address = server.accept()
        print("Connected with {}".format(str()))
        client.send('NUMBER'.encode('ascii'))
        number = client.recv(1024).decode('ascii')
        main_num[client] = number
        numbers.append(number)
        clients.append(client)
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


os.system('clear')
receive()