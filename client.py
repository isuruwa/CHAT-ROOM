#!/bin/python
#DEVELOPED BY DEVILMASTER
#Don't Be a Script-kiddie

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


def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1 / 10)


print(banner)
slowprint(colors.pink + "[CONNECTING] Connecting to server..." )
slowprint(colors.green + "[CONNECTED] Connected to server...")
nickname = input(colors.blue + "[+] Enter your username : ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = '127.0.0.1'
port = 4444
client.connect((server, port))


def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICKNAME':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            slowprint(bcolor.red + "[ERROR] An error occured!")
            client.close()
            break


def write():
    while True:
        message = '[{}] >> {}'.format(nickname, input(''))
        client.send(message.encode('ascii'))


receive_thread = threading.Thread(target=receive)
receive_thread.start()
write_thread = threading.Thread(target=write)
write_thread.start()

