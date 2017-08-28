from PyQt5.QtWidgets import *
import connToDatabase
import sys

class RegisterDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.showRegister()

    def showRegister(self):
        InfoLayout = QGridLayout()
        ButtonLayout = QHBoxLayout()

        self.RegisterButten = QPushButton('注册')
        self.RegisterButten.clicked.connect(self.RegisterToDatabase)
        
        self.QuitButton  = QPushButton('退出')
        self.QuitButton.clicked.connect(self.close)

        self.AccountLbl  = QLabel('账户：')
        self.AccountEdit = QLineEdit()

        
        self.PasswdLbl = QLabel('密码：')
        self.PasswdEdit = QLineEdit()
        self.PasswdEdit.setPlaceholderText('123')
        self.PasswdEdit.setEchoMode(QLineEdit.Password)

        self.rePasswdLbl = QLabel('重新密码：')
        self.rePasswdEdit = QLineEdit()
        self.rePasswdEdit.setPlaceholderText('123')
        self.rePasswdEdit.setEchoMode(QLineEdit.Password)

        self.MailLbl  = QLabel('邮箱：')
        self.MailEdit = QLineEdit()

        InfoLayout.addWidget(self.AccountLbl,0,0)
        InfoLayout.addWidget(self.AccountEdit,0,1)
        InfoLayout.addWidget(self.PasswdLbl,1,0)
        InfoLayout.addWidget(self.PasswdEdit,1,1)
        InfoLayout.addWidget(self.rePasswdLbl,2,0)
        InfoLayout.addWidget(self.rePasswdEdit,2,1)
        InfoLayout.addWidget(self.MailLbl,3,0)
        InfoLayout.addWidget(self.MailEdit,3,1)
        

        ButtonLayout.addWidget(self.RegisterButten)
        ButtonLayout.addWidget(self.QuitButton)
        

        mainLayout = QGridLayout(self)
        mainLayout.setSpacing(20)
        mainLayout.addLayout(InfoLayout, 0, 0)
        mainLayout.addLayout(ButtonLayout, 1, 0)

        
        self.resize(350, 200)
        self.setWindowTitle('Register')

    def RegisterToDatabase(self):
        self.ACCOUNT = self.AccountEdit.text()
        self.PASSWD = self.PasswdEdit.text()
        self.rePASSWD = self.rePasswdEdit.text()
        self.MAIL = self.MailEdit.text()
        if self.PASSWD == self.rePASSWD:
            conn = connToDatabase.connToDatabase('127.0.0.1','chatroot','000000','chatroom')
            conn.RegisterNewAccount(self.ACCOUNT,self.PASSWD,self.MAIL)
        else:
            passwdError_Message = QMessageBox.information(self,'error','password error')

    def ErrorMessage(self):
        pass
  

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RegisterDialog()
    ex.show()
    sys.exit(app.exec_())
