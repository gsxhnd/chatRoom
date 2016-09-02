from PyQt5.QtWidgets import *
import sys

class RegisterDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.showRegister()

    def showRegister(self):
        InfoLayout = QGridLayout()
        ButtonLayout = QHBoxLayout()

        self.RegisterButten = QPushButton('注册')
        
        self.QuitButton  = QPushButton('退出')
        self.QuitButton.clicked.connect(qApp.quit)

        self.AccountLbl  = QLabel('账户：')
        self.AccountEdit = QLineEdit()

        
        self.PasswdLbl = QLabel('密码：')
        self.PasswdEdit = QLineEdit()
        self.PasswdEdit.setPlaceholderText('123')

        self.rePasswdLbl = QLabel('re密码：')
        self.rePasswdEdit = QLineEdit()
        self.rePasswdEdit.setPlaceholderText('123')

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
  

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RegisterDialog()
    ex.show()
    sys.exit(app.exec_())
