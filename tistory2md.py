# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, sip
from PyQt5.QtCore import pyqtSignal, pyqtSlot, QObject, QThread 
from PyQt5.QtWidgets import *
from tistory2md_ui import Ui_Dialog
from PyQt5.QtGui import QIcon
from backup import BackUp
import os
import time
import platform



message = ''
blogName = ''
accessToken = ''
saveDir = ''
checkbox = {}
startNum = 0
endNum = 0
startBtn = None


class Worker(QThread):
    # // 시그널 객체를 하나 생성합니다.
    sig_message = pyqtSignal(str)
    sig_end = pyqtSignal()
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)


    @pyqtSlot()           
    def run(self):
        global message, blogName, accessToken, saveDir, checkbox, startNum, endNum
        backup = BackUp(blogName, accessToken, saveDir, checkbox)

        for i in range(startNum, endNum+1):    
            response = backup.start_backup(i)
            
            if response.status_code == 200 and response.json() != None:
                message = '[#'+str(i)+']'
                temp = backup.save_document(response.json())
                if len(temp) == 0:
                    temp = '...done!'
                # self.status.append('['+str(i)+']'+ message)
                message += temp
            elif response.status_code == 200 and response.json() == None:
                message = '[Error #'+str(i)+'] 비공개 카테고리 입니다.'
            else:
                # self.status.append('[Error #'+str(i)+']\n'+response.text)
                message = '[Error #'+str(i)+'] '+response.text

            # print(message)
            self.sig_message.emit(message)
            
        self.sig_end.emit()


class XDialog(QDialog, Ui_Dialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("tistory2md v1.0")

        self.startBtn.clicked.connect(self.start)
        self.stopBtn.clicked.connect(self.forceStop)
        self.saveDirBtn.clicked.connect(self.openDir)

        # self.stopBtn.setStyleSheet("color: red")
        # self.stopBtn.setEnabled(False)

        self.error_dialog = QtWidgets.QErrorMessage()
        if platform.system() == 'Windows':
            self.saveDir.setText(os.getcwd())
        elif platform.system() == 'Darwin':
            self.saveDir.setText(os.getcwd().split('tistory2md')[0])   

        self.worker = Worker()
        self.startBtn.setEnabled(True)


    def start(self):
        global message, blogName, accessToken, saveDir, checkbox, startNum, endNum
        
        self.status.clear()
        if self.inputValidation() == False:
            return

        checkbox = {'image':self.imageCheck.isChecked(), 'tag':self.tagCheck.isChecked(), 'youtube':self.youtubeCheck.isChecked()}
        blogName = self.blogName.text()
        accessToken = self.accessToken.text()
        saveDir = self.saveDir.text()
        startNum = int(self.startNum.text())
        endNum = int(self.endNum.text())


        self.startBtn.setEnabled(False)
        # self.stopBtn.setEnabled(True)
        # self.stopBtn.setStyleSheet("color: red")

        # self.worker.daemon=True
        self.worker.start()
        self.worker.sig_message.connect(self.status.appendPlainText)
        self.worker.sig_end.connect(self.endThread)



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

    def forceStop(self):
        if self.worker.isRunning():  
            self.worker.terminate()  
            del self.worker
            self.worker = Worker()

        # self.stopBtn.setEnabled(False)
        # self.stopBtn.setStyleSheet("color:")
        self.startBtn.setEnabled(True)

    def endThread(self):
        self.startBtn.setEnabled(True)
        # self.stopBtn.setEnabled(False)
        # self.stopBtn.setStyleSheet("color:")
        # del self.worker
        self.worker = Worker()
        if self.logCheck.isChecked():
            f = open('log.txt', 'w')
            f.write(self.status.toPlainText())

    def openDir(self):
        fname = QFileDialog.getExistingDirectory(self, 'Open Folder', os.getcwd())
        self.saveDir.setText(fname)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlg = XDialog()
    dlg.show()
    app.exec_()