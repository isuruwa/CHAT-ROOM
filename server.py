#!/bin/python
#DEVELOPED BY DEVILMASTER

import sys, time, socket, threading, os

os.system('clear')


class colors:
    blue = '\033[94m'
    cyan = '\033[96m'
    green = '\033[92m'
    red = '\033[31m'
    pink = '\033[35m'


banner = colors.cyan + """
  _______ _____ ______    ___  ____  ____  __  ___
 / ___/ // / _ /_  __/___/ _ \/ __ \/ __ \/  |/  /
/ /__/ _  / __ |/ / /___/ , _/ /_/ / /_/ / /|_/ /
\___/_//_/_/ |_/_/     /_/|_|\____/\____/_/  /_/

 [*] CHAT-ROOM - A SIMPLE CHAT SERVER [*]
 [*]    DEVELOPED BY DEVIL MASTER     [*]

"""
host = '127.0.0.1'
port = 4444

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []


def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1 / 10)


def broadcast(message):
    for client in clients:
        client.send(message)


def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(
                '{} left in the chatroom!\n'.format(nickname).encode('ascii'))
            nicknames.remove(nickname)
            break


def receive():
    while True:
        client, address = server.accept()
        slowprint(colors.green +
                  "[CONNECTED] Connected with {}".format(str(address)))
        client.send('NICKNAME'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)
        slowprint("[CLIENT] {}".format(nickname))
        broadcast("[CLIENT] {} joined in the chatroom!".format(
            nickname).encode('ascii'))
        #client.send('[!] Connected to the server...\n'.encode('ascii'))
        #client.send('\n[+] You can now start chatting...'.encode('ascii'))
        thread = threading.Thread(target=handle, args=(client, ))
        thread.start()


print(banner)
slowprint(colors.green + "[STARTED] Server is runing...")
slowprint(colors.pink + "[WAITING] Waiting for clients ...")
receive()

