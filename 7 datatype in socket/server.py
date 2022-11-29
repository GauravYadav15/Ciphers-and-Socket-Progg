import socket as so

def my_type (msg):
    try :
        msg = int(msg)
        if msg>0:
            return "+ INT"
        elif msg ==0:
            return "NEUTRAL INT"
        else:
            return "- INT"

    except:
        try :
            msg = float(msg)
            if msg>0:
                return "+ FLOAT"
            else :
                return "- FLOAT"
            

        except:
            if msg.isalpha():
                return "ALPHA ONLY"
            elif msg.isalnum():
                return "ALPHANUM"
            return "SPECIAL"


s = so.socket()
print("Connection made")

port = 8787
s.bind(('localhost',port))
admin = input("Enter name of admin : ")
s.listen(1)
print('Waiting for connections')

while True:
    c, addr = s.accept()
    while True:
        
            
        msg = c.recv(1024).decode()
        if msg == ";":
            break
        data_type = my_type(msg)
        print(data_type)
        c.send(bytes(f"type of your {data_type} ",'utf-8'))



