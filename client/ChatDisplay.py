# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore as core
import sys

class ChatDisplay(QDialog):
    def __init__(self):
        super().__init__()
        self.showchatRoom()

    def showchatRoom(self):
        self.layout = QGridLayout(self)
        self.sendButten = QPushButton('发送')
        self.inputContent = QLineEdit()
        self.chatText = QTextEdit()
        self.chatText.setReadOnly(True)
        # self.sendButten.clicked.connect(self.sendToServer)
        self.layout.addWidget(self.chatText, 0, 0, 5, 5)
        self.layout.addWidget(self.inputContent, 5, 0, 1, 4)
        self.layout.addWidget(self.sendButten, 5, 4)
        self.resize(400, 500)
        self.setWindowTitle('chatRoom')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ChatDisplay()
    ex.show()
    sys.exit(app.exec_())
