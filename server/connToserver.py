import pymysql.cursors

class connToserver():
    def __init__(self,HOST,USER,PASSWD,DBNAME):
        self.conn = pymysql.connect(host = HOST,user = USER,passwd = PASSWD,db = DBNAME,charset = 'utf8')
        self.cur = self.conn.cursor()

    def getUserpasswd(self,account):  
        """
        get user's password from database
        """
        self.cur.execute("select * from user_passwd where username = '%s' " %account)
        for each in self.cur:
            return each[2]
        self.conn.close()
