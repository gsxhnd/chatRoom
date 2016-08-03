import sys
import os
import user_config
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore as core




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
        # else:
        #     ip = ''
        #     port = ''
        #     account = ''
        #     password = ''



        """
        登录界面的设计
        """
        IpLbl = QLabel('IP：')
        self.IpEdit = QLineEdit('')
        self.IpEdit.setPlaceholderText('输入IP地址')
        
        PortLbl = QLabel('PORT：')
        self.PortEdit = QLineEdit('')
        self.PortEdit.setPlaceholderText('输入端口')

        AccountLbl = QLabel('账户：')
        self.AccountEdit = QLineEdit('')
        self.AccountEdit.setPlaceholderText('输入账户')

        PasswordLbl = QLabel('密码：')
        self.PasswordEdit = QLineEdit('')
        self.PasswordEdit.setEchoMode(QLineEdit.Password)
        self.PasswordEdit.setPlaceholderText('输入密码')

        # SecLbl = QLabel('加密方式')
        # SecCombo = QComboBox()
        # SecCombo.addItems(['没有实现', '没有实现', '没有实现'])
        #加密方式选择（未实现，先注释）


        """
        按钮动作
        """
        connectButton = QPushButton('连接')
        connectButton.clicked.connect(configout)
    
        quitButton = QPushButton('退出')
        quitButton.clicked.connect(qApp.quit)

        """
        界面布局
        """
        InfoLayout = QGridLayout()
        ButtonLayout = QHBoxLayout()
            
        InfoLayout.addWidget(IpLbl, 0, 0)
        InfoLayout.addWidget(self.IpEdit, 0, 1)
        InfoLayout.addWidget(PortLbl, 1, 0)
        InfoLayout.addWidget(self.PortEdit, 1, 1)
        InfoLayout.addWidget(AccountName, 2, 0)
        InfoLayout.addWidget(self.AccountEdit, 2, 1)
        InfoLayout.addWidget(PasswordLbl,3,0)
        InfoLayout.addWidget(self.Password,3,1)
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


        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = loginDialog()
    ex.show()
    sys.exit(app.exec_())
