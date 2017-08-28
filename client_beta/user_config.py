import os


def get_config(filename):
    readInfo = open(filename, 'rb')
    readInfoData = readInfo.readline()
    readInfo.close()
    getConfigData = eval(readInfoData)
    return (getConfigData['IP'],getConfigData['PORT'],getConfigData['ACCOUNT'],getConfigData['PASSWORD'])

def configOut(IP,PORT,ACCOUNT,PASSWORD):
    configContent = {'IP': IP, 'PORT': PORT, 'ACCOUNT':ACCOUNT,'PASSWORD':PASSWORD}
    configData = str(configContent)
    output = open('config.ini', 'w+')
    output.write(configData)
    output.close()