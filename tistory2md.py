# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *
from tistory2md_ui import Ui_Dialog

class XDialog(QDialog, Ui_Dialog):
    def __init__(self):
        QDialog.__init__(self)
        # setupUi() 메서드는 화면에 다이얼로그 보여줌
        self.setupUi(self)
        self.startBtn.clicked.connect(self.sayHello)


    def sayHello(self):
        self.saveDir.setText('Hello world!')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlg = XDialog()
    dlg.show()
    app.exec_()