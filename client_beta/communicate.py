import socket
from PyQt5.QtWidgets import *

class Sockconnect():
    def __init__(self,IP,PORT):
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.s.connect((IP,PORT))

    def checkLogin(self,data):
        self.s.send(data)
            
    def sendToserver(self):
        self.s.send(data)
    
    def recvFromserver(self):
        data = self.s.recv(1024).decode()
        return data

# if __name__ == '__main__':
    