import socket
import connToserver

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
conn_database = connToserver.connToserver('192.168.84.140','chatroot','000000','chat')
conn_getuserpasswd = conn_database.getUserpasswd

while 1:
    count = 0
    conn,addr = s.accept()
    print('connected with ' + addr[0] + ':' + str(addr[1]))
    data = conn.recv(1024).decode()
    print(data)
    checkdata = eval(data)
    username = checkdata['username']
    print(username)
    info = conn_getuserpasswd(username)
    print(info)
    if info == checkdata['password'] :
        # conn.send('pass')
        print('pass')
    else:
        count = count + 1
        # conn.send('faild')
        print('faild')