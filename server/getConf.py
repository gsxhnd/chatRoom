import os
import sys

import configparser


class getConf():
    """
    get configuration from file's name is [confName].
    """
    def __init__(self,confName):
        if os.path.exists(os.path.join(sys.path[0],confName)):
            self.confName = confName
        else:
            print("no file")
    
    def getValue(self,*keys):
        cp = configparser.ConfigParser()
        cp.read(os.path.join(sys.path[0],self.confName))
        confValue = cp[keys[0]][keys[1]]
        return(confValue)
if __name__ == '__main__':
    # a = getConf("server.conf",'Database','DBName')
    a = getConf("server.conf")
    dbname = a.getValue('Database','DBName')
    dbuser = a.getValue('Database','DBUser')
    dbpasswd = a.getValue('Database','DBPasswd')
    print(a,dbname,dbuser,dbpasswd)