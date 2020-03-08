# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from tistory2md_ui import Ui_Dialog
from backup import BackUp
import os

class XDialog(QDialog, Ui_Dialog):
    def __init__(self):
        QDialog.__init__(self)
        # setupUi() 메서드는 화면에 다이얼로그 보여줌
        self.setupUi(self)
        self.startBtn.clicked.connect(self.start)
        self.error_dialog = QtWidgets.QErrorMessage()
        self.saveDir.setText(os.getcwd())
    def start(self):
        self.status.clear()
        if self.inputValidation() == False:
            return

        backup = BackUp(self.blogName.text(), self.accessToken.text(), self.saveDir.text())

        for i in range(int(self.startNum.text()), int(self.endNum.text())+1):    
            response = backup.start_backup(i)

            if response.status_code == 200:
                backup.save_document(response.json())
                self.status.append(str(i)+'...done.')
            else:
                self.status.append('[Error #'+str(i)+']\n'+response.text)


    def inputValidation(self):
        
        
        # isEmpty check
        if self.blogName.text() == "":
            self.error_dialog.showMessage('블로그 주소를 입력해주세요.')
            self.error_dialog.exec_()
            return False
        if self.accessToken.text() == "":
            self.error_dialog.showMessage('Access token을 입력해주세요.')
            self.error_dialog.exec_()
            return False
        if self.startNum.text() == "" or self.endNum.text() == "":
            self.error_dialog.showMessage('문서 번호를 입력해주세요.')
            self.error_dialog.exec_()
            return False
        
        # valid check
        if self.startNum.text() != "":
            try:
                int(self.startNum.text())
            except ValueError:
                self.error_dialog.showMessage('문서 번호는 숫자만 넣어주세요.')
                self.error_dialog.exec_()
                return False
        if self.endNum.text() != "":
            try:
                int(self.endNum.text())
            except ValueError:
                self.error_dialog.showMessage('문서 번호는 숫자만 넣어주세요.')
                self.error_dialog.exec_()
                return False

        if int(self.startNum.text()) > int(self.endNum.text()):
            self.error_dialog.showMessage('문서 시작번호는 끝번호보다 작은 수여야 합니다.')
            self.error_dialog.exec_()
            return False


        return True


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlg = XDialog()
    dlg.show()
    app.exec_()