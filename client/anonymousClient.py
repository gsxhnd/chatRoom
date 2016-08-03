# -*- coding: utf-8 -*-
import sys
import os
import socket
import threading
import datetime
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
        if os.path.exists('config.ini'):
            showconfig = showConfig.get_config('config.ini')
            ip = showconfig[0]
            port = showconfig[1]
            nick = showconfig[2]
        else:
            ip = ''
            port = ''
            nick = ''

        IpLbl = QLabel('IP:')
        self.IpEdit = QLineEdit('')
        self.IpEdit.setPlaceholderText('输入IP地址')
        
        PortLbl = QLabel('PORT:')
        self.PortEdit = QLineEdit('')
        self.PortEdit.setPlaceholderText('输入端口')

        NickName = QLabel('昵称:')
        self.NickEdit = QLineEdit()
        self.NickEdit.setPlaceholderText('输入昵称')

        SecLbl = QLabel('加密方式')
        SecCombo = QComboBox()
        SecCombo.addItems(['没有实现', '没有实现', '没有实现'])

        connectButton = QPushButton('连接')
        connectButton.clicked.connect(self.configOut)
    
        quitButton = QPushButton('退出')
        quitButton.clicked.connect(qApp.quit)

        InfoLayout = QGridLayout()
        ButtonLayout = QHBoxLayout()
            
        InfoLayout.addWidget(IpLbl, 0, 0)
        InfoLayout.addWidget(self.IpEdit, 0, 1)
        InfoLayout.addWidget(PortLbl, 1, 0)
        InfoLayout.addWidget(self.PortEdit, 1, 1)
        InfoLayout.addWidget(NickName, 2, 0)
        InfoLayout.addWidget(self.NickEdit, 2, 1)
        InfoLayout.addWidget(SecLbl, 3, 0)
        InfoLayout.addWidget(SecCombo, 3, 1)
        ButtonLayout.addWidget(connectButton)
        ButtonLayout.addWidget(quitButton)

        mainLayout = QGridLayout(self)
        mainLayout.setSpacing(20)
        mainLayout.addLayout(InfoLayout, 0, 0)
        mainLayout.addLayout(ButtonLayout, 1, 0)

        self.resize(350, 270)
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
            ipErrorMessage = QMessageBox.information(self, 'error', '请输入正确的IP地址')
        elif self.getPORT == '':
            portErrorMessage = QMessageBox.information(self, 'error', '请输入正确的端口')
        elif self.getNICK == '':
            nickErrorMessage = QMessageBox.information(self, 'error', '请输入昵称')
        else:
            
            configContent = {'IP': self.getIP, 'PORT': self.getPORT, 'NICKNAME': self.getNICK}

            configData = str(configContent)
            output = open('config.ini', 'w+')
            output.write(configData)
            output.close()

            self.close()

            showchatroom = ChatRoom()
            showchatroom.show()
            showchatroom.exec_()


class showConfig():
    def get_config(filename):
        if os.path.exists(filename):
            readInfo = open('config.ini', 'rb')
            readInfoData = readInfo.readline()
            readInfo.close()
            getConfigData = eval(readInfoData)
            return (getConfigData['IP'],getConfigData['PORT'],getConfigData['NICKNAME'])



class ChatRoom(QDialog):
    def __init__(self):
        super().__init__()
        self.showchatRoom()
        showconfig = showConfig.get_config('config.ini')
        host = showconfig[0]
        port = int(showconfig[1])
        self.nickname = showconfig[2]
        inString = ''
        outString = ''
        self.SockData = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.SockData.connect((host, port))
        self.SockData.send(self.nickname.encode())

        self.timer = core.QTimer()
        self.message = []

        self.timer.timeout.connect(self.showChat)
        self.timer.start(1000)

        thin = threading.Thread(target=self.recvFromServer)
        thin.setDaemon(True)
        thin.start()

    def sendToServer(self):
        global outString
        outString = self.inputContent.text()
        outString = self.nickname + ' ' + dateNow + ': \n' + outString
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

    def showchatRoom(self):
        self.layout = QGridLayout(self)
        self.sendButten = QPushButton('发送')
        self.inputContent = QLineEdit()
        self.chatText = QTextEdit()
        self.chatText.setReadOnly(True)
        self.sendButten.clicked.connect(self.sendToServer)
        self.layout.addWidget(self.chatText, 0, 0, 5, 5)
        self.layout.addWidget(self.inputContent, 5, 0, 1, 4)
        self.layout.addWidget(self.sendButten, 5, 4)
        self.resize(400, 500)
        self.setWindowTitle('chatRoom')


# class cryptoMessage():
#     def savekey(self):
#         (self.pub_key,self.priv_key) = rsa.newkeys(1024)
#         rsa.PrivateKey.save_pkcs1
#         rsa.PublicKey.save_pkcs1
    
#     # def sendCheckToServer(self):
#         sendCheckToserver = self.SockData.send(self.pub_key)
#     # def recvCheckFromServer(self):
#         recvCheckFromServer = self.SockData.recv(1024).decode()

        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = loginDialog()
    ex.show()
    sys.exit(app.exec_())
