import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore as core

import user_config
import ChatDisplay



class loginDialog(QWidget):
    def __init__(self):
        super().__init__()
        self.showDialog()
    
    def showDialog(self):

        """
        读取配置文件信息
        """
        
        if os.path.exists('config.ini'):
            getdata = user_config.get_config('config.ini')
            ip = getdata[0]
            port = getdata[1]
            account = getdata[2]
            password = getdata[3]
        else:
            ip = ''
            port = ''
            account = ''
            password = ''



        """
        登录界面的设计
        """
        IpLbl = QLabel('IP：')
        IpEdit = QLineEdit(ip)
        IpEdit.setPlaceholderText('输入IP地址')
        
        PortLbl = QLabel('PORT：')
        PortEdit = QLineEdit(port)
        PortEdit.setPlaceholderText('输入端口')

        AccountLbl = QLabel('账户：')
        AccountEdit = QLineEdit(account)
        AccountEdit.setPlaceholderText('输入账户')

        PasswordLbl = QLabel('密码：')
        PasswordEdit = QLineEdit(password)
        PasswordEdit.setEchoMode(QLineEdit.Password)
        PasswordEdit.setPlaceholderText('输入密码')

        # SecLbl = QLabel('加密方式')
        # SecCombo = QComboBox()
        # SecCombo.addItems(['没有实现', '没有实现', '没有实现'])
        #加密方式选择（未实现，先注释）

        """
        按钮动作
        """
        self.IP = IpEdit.text()
        self.PORT = PortEdit.text()
        self.ACCOUNT = AccountEdit.text()
        self.PASSWORD = PasswordEdit.text()

        

        connectButton = QPushButton('连接')
        connectButton.clicked.connect(self.configure)
        #写入配置
        connectButton.clicked.connect(self.showChatDisplay)
        quitButton = QPushButton('退出')
        quitButton.clicked.connect(qApp.quit)

        """
        界面布局
        """
        InfoLayout = QGridLayout()
        ButtonLayout = QHBoxLayout()
            
        InfoLayout.addWidget(IpLbl, 0, 0)
        InfoLayout.addWidget(IpEdit, 0, 1)
        InfoLayout.addWidget(PortLbl, 1, 0)
        InfoLayout.addWidget(PortEdit, 1, 1)
        InfoLayout.addWidget(AccountLbl, 2, 0)
        InfoLayout.addWidget(AccountEdit, 2, 1)
        InfoLayout.addWidget(PasswordLbl,3,0)
        InfoLayout.addWidget(PasswordEdit,3,1)
        # InfoLayout.addWidget(SecLbl, 4, 0)
        # InfoLayout.addWidget(SecCombo, 4, 1)
        #加密方式布局（未实现，先注释）
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
        """
        使界面在显示屏中心显示
        """
        showFrame = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        showFrame.moveCenter(centerPoint)
        self.move(showFrame.topLeft())

    def showChatDisplay(self):
        """
        关闭登录界面并打开聊天窗口
        """
        self.close()
        showchatdisplay = ChatDisplay.ChatDisplay()
        showchatdisplay.show()
        showchatdisplay.exec_()

    def configure(self):
        """
        将信息写入配置文件
        """
        configout = user_config.configOut
        configout(self.IP,self.PORT,self.ACCOUNT,self.PASSWORD)

        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = loginDialog()
    ex.show()
    sys.exit(app.exec_())
