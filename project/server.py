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
                print(type(message))
                if client_1 != client:
                    message = bytes(f"b'{main_num[client_1]}'")
            broadcast(message, client)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            client = clients[index]
            clients.remove(client)
            break


def receive():
    while True:
        client, address = server.accept()
        print("Connected with {}".format(str()))
        client.send('NUMBER'.encode('ascii'))
        number = client.recv(1024).decode('ascii')
        if len(numbers) < 2:
            main_num[client] = number
            numbers.append(number)
            clients.append(client)
            print("Client is {}".format(client))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


os.system('clear')
receive()