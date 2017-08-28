import pymysql.cursors
import getConf

class connDatabase():
    def __init__(self,*sqlKey):
        # print(sqlKey)
        self.conn = pymysql.connect(
            host=sqlKey[0],user = sqlKey[2],passwd = sqlKey[3],db = sqlKey[1])
        self.cur = self.conn.cursor()

    def getUserpasswd(self,account):  
        """
        get user's password from database
        """
        # pass1 = "zabbix"
        self.cur.execute("select * from users where alias = '%s' " %account)
        for each in self.cur:
            return each[2]
            # return(each)
        self.conn.close()

    def RegisterAccount(self,ACCOUNT,PASSWD,MAIL):
        """
        dad
        """
        sql_content = "insert into user_passwd (username,password,mail) values('%s','%s','%s')" %(ACCOUNT,PASSWD,MAIL)
        self.cur.execute(sql_content)
        self.conn.commit()
        self.cur.close()
        self.conn.close()

if __name__ == '__main__':
    serverName = "server.conf"
    ServerConfiguration = getConf.getConf(serverName)

    DBHost = ServerConfiguration.getValue("DataBase","DBHost")
    DBName = ServerConfiguration.getValue("DataBase","DBName")
    DBUser = ServerConfiguration.getValue("DataBase","DBUser")
    DBPasswd = ServerConfiguration.getValue("DataBase","DBPasswd")
    
    a = connDatabase(DBHost,DBName,DBUser,DBPasswd)
    passwd = a.getUserpasswd("Admin")
    print(passwd)