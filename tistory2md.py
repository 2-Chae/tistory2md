# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, sip
from PyQt5.QtCore import pyqtSignal, pyqtSlot, QObject, QThread 
from PyQt5.QtWidgets import *
from tistory2md_ui import Ui_Dialog
from PyQt5.QtGui import QIcon
from backup import BackUp
import time
import os

class Worker(QObject):
    sig_message = pyqtSignal(str)
    sig_end = pyqtSignal()
    sig_clearStatus = pyqtSignal()

    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)

    @pyqtSlot(dict)
    def set(self, d):
        self.blogName = d['blogName']
        self.accessToken = d['accessToken']
        self.saveDir = d['dir']
        self.checkbox = d['checkbox']
        self.startNum = d['startNum']
        self.endNum = d['endNum']


    def startWork(self):  
        self.sig_clearStatus.emit()
        backup = BackUp(self.blogName, self.accessToken, self.saveDir, self.checkbox)

        for i in range(self.startNum, self.endNum+1):                                        
            response = backup.start_backup(i)
            message = ''
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

            self.sig_message.emit(message)     
        self.sig_end.emit()


class Mid(QObject):
    sig_settings = pyqtSignal(dict)

    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)

        self.gui = QtWidgets.QDialog()
        self.ui = Ui_Dialog()       
        self.ui.setupUi(self.gui)
        
        self.worker = Worker()
        self.worker_thread = QThread()
        self.worker.moveToThread(self.worker_thread)
        self.worker_thread.start()
        # self.worker_thread.daemon = True

        self._connectSignals()
        self.gui.show()

    def transmit(self):
        if self.ui.inputValidation() == False:
            return
        
        d = {}
        d['checkbox'] = {'image':self.ui.imageCheck.isChecked(), 'tag':self.ui.tagCheck.isChecked(), 'youtube':self.ui.youtubeCheck.isChecked()}
        d['blogName'] = self.ui.blogName.text()
        d['accessToken'] = self.ui.accessToken.text()
        d['dir'] = self.ui.saveDir.text()
        d['startNum'] = int(self.ui.startNum.text())
        d['endNum'] = int(self.ui.endNum.text())

        self.ui.pushSettingBtn()
        self.sig_settings.emit(d)

    def _connectSignals(self):
        self.ui.startBtn.clicked.connect(self.worker.startWork)
        self.ui.settingBtn.clicked.connect(self.transmit)
        self.ui.stopBtn.clicked.connect(self.forceWorkerReset)
        self.ui.saveDirBtn.clicked.connect(self.openDir)

        self.sig_settings.connect(self.worker.set)

        self.worker.sig_clearStatus.connect(self.pushStart)
        self.worker.sig_message.connect(self.ui.status.appendPlainText)
        self.worker.sig_end.connect(self.forceWorkerReset)

    def openDir(self):
        fname = QFileDialog.getExistingDirectory(self.gui, 'Open Folder', os.getcwd())
        self.ui.saveDir.setText(fname)

    @pyqtSlot()
    def pushStart(self):
        self.ui.pushStartBtn()

    def forceWorkerReset(self):
        if self.worker_thread.isRunning():  
            self.worker_thread.terminate()  
            self.worker_thread.wait()       
            self.worker_thread.start()  
        self.ui.buttonInit()
        f = open('log.txt', 'w')
        f.write(self.ui.status.toPlainText())

        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mid = Mid(app)
    app.exec_()