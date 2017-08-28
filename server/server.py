import socket
import connDatabase
import getConf

# HOST = input("input the server's ip address: ")
# port = input("input the server's port: ")
# PORT = int(port)
serverName = "server.conf"
ServerConfiguration = getConf.getConf(serverName)
HOST = ServerConfiguration.getValue("Default","HOST")
PORT = ServerConfiguration.getValue("Default","PORT")

DBHost = ServerConfiguration.getValue("DataBase","DBHost")
DBName = ServerConfiguration.getValue("DataBase","DBName")
DBUser = ServerConfiguration.getValue("DataBase","DBUser")
DBPasswd = ServerConfiguration.getValue("DataBase","DBPasswd")



s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('Socket created')
s.bind((HOST,int(PORT)))
s.listen(10)
print('Socket now listening')
connDatabase = connDatabase.connDatabase(DBHost,DBName,DBUser,DBPasswd)
conn_getuserpasswd = connDatabase.getUserpasswd

while 1:
    count = 0
    conn,addr = s.accept()
    print('connected with ' + addr[0] + ':' + str(addr[1]))
    data = conn.recv(1024).decode()
    print(data)
    checkdata = eval(data)
    username = checkdata['username']
    checkPasswd = conn_getuserpasswd(username)
    if checkPasswd == checkdata['password'] :
        pass_login = 'pass'
        conn.send(pass_login.encode())
    else:
        count = count + 1
        pass_faild  = 'faild'
        conn.send(pass_faild.encode())