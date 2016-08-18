import socket

class Sockconnect():
    def __init__(self,IP,PORT):
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.s.connect((IP,PORT))
    
    def checkLogin(self,ACCOUNT,PASSWORD):
        self.s.send(ACCOUNT.encode(),PASSWORD.encode())

    def sendToserver(self):
        pass
    
    def recvFromserver(self):
        pass


# if __name__ == '__main__':

    