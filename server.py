import socket
import pymysql.cursors

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

def conn_databaes(acccount):
    conn = pymysql.connect(host = '192.168.84.140' ,user = 'chatroot' ,passwd = '000000' ,db = 'chat' ,charset = 'utf8')
    cur = conn.cursor()
    cur.execute("select * from user_passwd where username = '%s' " %acccount)
    for each in cur:
        return each[2]
while 1:
    conn,addr = s.accept()
    print('connected with ' + addr[0] + ':' + str(addr[1]))
    data = conn.recv(1024).decode()
    print(data)
    checkdata = eval(data)
    username = checkdata['username']
    info = conn_databaes(username)
    print(info)