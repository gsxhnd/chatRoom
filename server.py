import socket

# HOST = input("input the server's ip address: ")
# port = input("input the server's port: ")
# PORT = int(port)

HOST = '127.0.0.1'
PORT = 8888

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('Socket created')
s.bind((HOST,PORT))
s.listen(10)
print('Socket now listening')

while 1:
    conn,addr = s.accept()
    print('connected with ' + addr[0] + ':' + str(addr[1]))
    data = conn.recv(1024).decode()
    print(data)