# -*- coding: utf-8 -*-
import sys,os,socket,threading,datetime
#from PyQt5.QtWidgets import (QWidget,QApplication,QMainWindow,qApp,QAction,QPushButton
#                               ,QAction,QProgressDialog)
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore as core


dateNow = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
class loginDialog(QWidget):
    def __init__(self):
        super().__init__()
        self.showDialog()
    
    def showDialog(self):

        getdata = showConfig()
        if os.path.exists(showConfig.filename):
            ip = getdata.getDataIP
            port = getdata.getDataPORT
            nick = getdata.getDataNICK
        else:
            ip = '输入IP地址'
            port = '输入端口'
            nick = '输入昵称'

        IpLbl = QLabel('IP')
        self.IpEdit = QLineEdit(ip)
        PortLbl = QLabel('PORT')
        self.PortEdit = QLineEdit(port)
        NickName = QLabel('昵称')
        self.NickEdit = QLineEdit(nick)
        SecLbl = QLabel('加密方式')
        SecCombo = QComboBox()
        SecCombo.addItems(['没有实现','没有实现','没有实现'])



        connectButton = QPushButton('连接')
        connectButton.clicked.connect(self.configOut)
    
        quitButton = QPushButton('退出')
        quitButton.clicked.connect(qApp.quit)
        
            
        InfoLayout = QGridLayout()
        ButtonLayout = QHBoxLayout()
            
        InfoLayout.addWidget(IpLbl,0,0)
        InfoLayout.addWidget(self.IpEdit,0,1)
        InfoLayout.addWidget(PortLbl,1,0)
        InfoLayout.addWidget(self.PortEdit,1,1)
        InfoLayout.addWidget(NickName,2,0)
        InfoLayout.addWidget(self.NickEdit,2,1)
        InfoLayout.addWidget(SecLbl,3,0)
        InfoLayout.addWidget(SecCombo,3,1)
        ButtonLayout.addWidget(connectButton)
        ButtonLayout.addWidget(quitButton)
            


        mainLayout = QGridLayout(self)
        mainLayout.setSpacing(20)
        mainLayout.addLayout(InfoLayout,0,0)
        mainLayout.addLayout(ButtonLayout,1,0)


        self.resize(350,270)
        self.showCenter()
        self.setWindowTitle('登录')
            
            

    def showCenter(self):
        showFrame = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        showFrame.moveCenter(centerPoint)
        self.move(showFrame.topLeft())
        
    def configOut(self):

        self.getIP = self.IpEdit.text()
        self.getPORT = self.PortEdit.text()
        self.getNICK = self.NickEdit.text()


        if self.getIP == '':
            ipErrorMessage = QMessageBox.information(self,'error','请输入正确的IP地址')
        elif self.getPORT == '':
            portErrorMessage = QMessageBox.information(self,'error','请输入正确的端口')
        elif self.getNICK == '':
            nickErrorMessage = QMessageBox.information(self,'error','请输入昵称')
        else:
            
            configContent = {'IP':self.getIP,'PORT':self.getPORT,'NICKNAME':self.getNICK}

            configData = str(configContent)
            output = open('config.ini','w+')
            output.write(configData)
            output.close()

            self.close()

            showchatroom = showChatRoom()
            showchatroom.show()
            showchatroom.exec_()
        
            
            


class showConfig():
    # global getDataIP
    # global getDataPORT
    # global getDataNICK
    filename = 'config.ini'
    if os.path.exists(filename):
        getInfo = open('config.ini','rb')
        getInfoData = getInfo.readline()
        getInfo.close()


        getConfigData = eval(getInfoData)
        getDataIP = getConfigData['IP']
        getDataPORT = getConfigData['PORT']
        getDataNICK = getConfigData['NICKNAME']


class showChatRoom(QDialog):
    def __init__(self):
        super().__init__()
        self.chatRoom()
        
        getInfo = open('config.ini','rb').readline()
        getData = eval(getInfo)
        host = getData['IP']
        port = int(getData['PORT'])
        self.nickname = getData['NICKNAME']
        inString = ''
        outString = ''
        self.SockData = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.SockData.connect((host,port))
        self.SockData.send(self.nickname.encode())

        self.timer = core.QTimer()
        self.message = []

        self.timer.timeout.connect(self.showChat)
        self.timer.start(1000)

        thin = threading.Thread(target = self.recvFromServer)
        thin.setDaemon(True)
        thin.start()
      

    def sendToServer(self):
        global outString
        outString = self.inputContent.text()
        outString = self.nickname + ' ' +dateNow +': \n' + outString
        self.inputContent.setText('')
        try:
            self.SockData.send(outString.encode())
        except:
            self.exit()
        


    def recvFromServer(self):
        while True:
            try:
                data = self.SockData.recv(1024).decode()
                if not data:
                    self.exit()
                self.message.append(data)
                
            except:
                break

    def exit(self):
        self.SockData.close()
        sys.exit()
    
    def showChat(self):
        for m in self.message:
            self.chatText.append(m)
        self.message = []




    def chatRoom(self):
        self.layout = QGridLayout(self)
        self.sendButten = QPushButton('发送')
        self.inputContent = QLineEdit()
        self.chatText = QTextEdit()
        self.sendButten.clicked.connect(self.sendToServer)
        self.layout.addWidget(self.chatText,0,0,5,5)
        self.layout.addWidget(self.inputContent,5,0,1,4)
        self.layout.addWidget(self.sendButten,5,4)
        

        self.resize(400,500)
        self.setWindowTitle('chatRoom')
        
        
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = loginDialog()
    ex.show()
    sys.exit(app.exec_())
    