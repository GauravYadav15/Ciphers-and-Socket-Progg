import socket

c = socket.socket()
port = 8787


c.connect(('localhost',port))
while 1:
    msg = input('Enter your message : ')

    if msg==";" :
        c.close()
        break

    c.send(bytes(msg,'utf-8'))

    print(c.recv(1024).decode())