import os
import socket
import threading
import time

host = '127.0.0.1'
port = 5097

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(2)

clients = []
numbers = []
main_num = {}


def broadcast(message):
    for client in clients:
        client.send(message)


def handle(client):
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message != 'prewinner':
                for client_1 in clients:
                    if client_1 != client:
                        message += ','
                        message += f'{main_num[client_1]}'
            message = message.encode('ascii')
            broadcast(message)
        except:
            print('close')
            index = clients.index(client)
            client = clients[index]
            client.close()
            clients.remove(client)
            break


def receive():
    while len(clients)<2:
        client, address = server.accept()
        print("Connected with {}".format(str(client)))
        client.send('NUMBER'.encode('ascii'))
        number = client.recv(1024).decode('ascii')
        main_num[client] = number
        numbers.append(number)
        clients.append(client)
        if len(clients) == 1:
            time.sleep(1)
            message = 'nostartgame'.encode('ascii')
            broadcast(message)
        elif len(clients) == 2:
            time.sleep(1)
            message = 'startgame'
            clients[0].send(message.encode('ascii'))
        print(len(clients))
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


os.system('cls')
receive()