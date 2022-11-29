def generateTable():
    arr = [[0 for i in range(256)] for j in range(256)] 
    
    ch = '\n'
    for i in range(256):
        arr[0][i] = ch
        ch = chr(ord(ch)+1)
    
    for i in range (1,256):
        for j in range (0,256):
            arr[i][j] = arr[i-1][(j+1)%256]

    return arr

def genKey(msg, key):
    keyword = ""
    keyword += key*(len(msg)//len(key))
    
    keyword += key[0:len(msg)%len(key)]

    return keyword

def cipher(msg, key):
    passkey  = genKey(msg, key)
    arr = generateTable()
    secret = ""
    for i in range(0,len(msg)):
        secret += arr[ord(passkey[i])][ord(msg[i])]

    return secret

def decipher(msg, key):
    passkey = genKey(msg, key)
    arr = generateTable()
    unsecret = ""

    for i in range(len(passkey)):
        for j in range(256):
            if arr[ord(passkey[i])][j] == msg[i]:
                unsecret += chr(j)

    return unsecret




