from PyQt5 import QtWidgets
class showMessageBox(QtWidgets):
    def __init__(self):
        super().__init__()
    def error(self):
        error_message = QMessageBox.information(self,'rr')