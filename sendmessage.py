import socket
import rsa

def Main():
    host = '192.168.20.8'
    port = 42421
    s = socket.socket()
    s.bind((host, port))

    s.listen(1)
    c, addr = s.accept()
    while True:
        data = c.recv(1024)
        if not data:
            break
        data = data.decode()
        print(data)
        c.send(data.encode())
    
    c.close()

if __name__ == '__main__':
    Main()
