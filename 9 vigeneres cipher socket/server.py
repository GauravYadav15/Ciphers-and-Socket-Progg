import socket as so
from utils import *



if __name__ == '__main__':

    
    s = so.socket()
    print("Connection made")

    port = 8787
    s.bind(('localhost',port))
    admin = input("Enter name of admin : ")
    key = input("Enter key : ")
    s.listen(1)
    print('Waiting for connections')

    while True:
        c, addr = s.accept()
        while True:
            
                
            msg = c.recv(1024).decode()
            if msg == ";":
                break
            unsecret = decipher(msg, key)
            
            c.send(bytes(f"your decrypted msg {unsecret} ",'utf-8'))



