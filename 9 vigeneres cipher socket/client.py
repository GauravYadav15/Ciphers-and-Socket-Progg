import socket
from utils import *

def generateTable():
    arr = [[]]
    c = '\n'
    for j in range (0,256):
        arr[0][j] = c
        c = c + 1

    for i in range (1,256):
        for j in range (0,256):
            arr[i][j] = arr[i-1][(j+1)%256]
    
    print(arr)

if __name__ == '__main__':

    c = socket.socket()
    port = 8787

    print("Enter your messages from (a to z) in lower case")
    c.connect(('localhost',port))
    while 1:
        msg = input('Enter your message : ')
        key = input('Enter your key :')
        if msg==";" :
            c.close()
            break

        secret = cipher(msg,key)
        print('Your secret msg ',secret)
        c.send(bytes(secret,'utf-8'))

        print(c.recv(1024).decode())