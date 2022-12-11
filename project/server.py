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
            print(str(client)[:10], message)
            if message == 'endgame':
                print(str(client)[:10], ':', message, 'remove client')
                index = clients.index(client)
                client = clients[index]
                clients.remove(client)
            else:
                print(str(client)[:10], ':', message, 'else doing')
                if message != 'prewinner' and message != 'endgame':
                    print(str(client)[:10], ':', message, 'message != "prewinner" and message != "endgame"')
                    for client_1 in clients:
                        if client_1 != client:
                            message += ','
                            message += f'{main_num[client_1]}'
                print('send message to clients')
                message = message.encode('ascii')
                broadcast(message)
        except:
            print('except')
            index = clients.index(client)
            client = clients[index]
            client.close()
            clients.remove(client)
            print('len clients', len(clients))
            if len(clients) == 1:
                print('len(clients) == 1', len(clients))
                message = 'goout'.encode('ascii')
                broadcast(message)
            break


def receive():
    while True:
        client, address = server.accept()
        print("Connected with {}".format(str(client), len(clients)))
        client.send('NUMBER'.encode('ascii'))
        number = client.recv(1024).decode('ascii')
        main_num[client] = number
        numbers.append(number)
        clients.append(client)
        print('len clients', len(clients))
        if len(clients) == 1:
            print('send nostartgame')
            time.sleep(1)
            message = 'nostartgame'.encode('ascii')
            broadcast(message)
        elif len(clients) == 2:
            print('send startgame')
            time.sleep(1)
            message = 'startgame'
            clients[0].send(message.encode('ascii'))
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


os.system('cls')
receive()