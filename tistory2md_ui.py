# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tistory2md.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, pyqtSlot
import os
import platform

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(586, 350)

        self.error_dialog = QtWidgets.QErrorMessage()
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 541, 311))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_12.addWidget(self.label_3)
        self.blogName = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.blogName.setObjectName("blogName")
        self.horizontalLayout_12.addWidget(self.blogName)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_12.addWidget(self.label_4)
        self.horizontalLayout_12.setStretch(1, 2)
        self.horizontalLayout_12.setStretch(2, 1)
        self.horizontalLayout.addLayout(self.horizontalLayout_12)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.accessToken = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.accessToken.setObjectName("accessToken")
        self.horizontalLayout_2.addWidget(self.accessToken)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 4)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_15 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_13.addWidget(self.label_15)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.startNum = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.startNum.setObjectName("startNum")
        self.horizontalLayout_16.addWidget(self.startNum)
        self.label_16 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_16.addWidget(self.label_16)
        self.endNum = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.endNum.setObjectName("endNum")
        self.horizontalLayout_16.addWidget(self.endNum)
        self.horizontalLayout_13.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_13.setStretch(0, 1)
        self.horizontalLayout_13.setStretch(1, 4)
        self.verticalLayout.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_17 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_14.addWidget(self.label_17)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.saveDir = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.saveDir.setObjectName("saveDir")
        self.horizontalLayout_15.addWidget(self.saveDir)
        self.saveDirBtn = QtWidgets.QToolButton(self.verticalLayoutWidget)
        self.saveDirBtn.setObjectName("saveDirBtn")
        self.horizontalLayout_15.addWidget(self.saveDirBtn)
        self.horizontalLayout_14.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_14.setStretch(0, 1)
        self.horizontalLayout_14.setStretch(1, 4)
        self.verticalLayout.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.imageCheck = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.imageCheck.setObjectName("imageCheck")
        self.horizontalLayout_3.addWidget(self.imageCheck)
        self.tagCheck = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.tagCheck.setObjectName("tagCheck")
        self.horizontalLayout_3.addWidget(self.tagCheck)
        self.youtubeCheck = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.youtubeCheck.setObjectName("youtubeCheck")
        self.horizontalLayout_3.addWidget(self.youtubeCheck)
        self.settingBtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.settingBtn.setAutoDefault(False)
        self.settingBtn.setObjectName("settingBtn")
        self.horizontalLayout_3.addWidget(self.settingBtn)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(2, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.status = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.status.setReadOnly(True)
        self.status.setPlainText("")
        self.status.setObjectName("status")
        self.verticalLayout.addWidget(self.status)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.stopBtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.stopBtn.setEnabled(False)
        self.stopBtn.setAutoDefault(False)
        self.stopBtn.setObjectName("stopBtn")
        self.horizontalLayout_4.addWidget(self.stopBtn)
        self.startBtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.startBtn.setEnabled(False)
        self.startBtn.setAutoDefault(False)
        self.startBtn.setObjectName("startBtn")
        self.horizontalLayout_4.addWidget(self.startBtn)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.retranslateUi(Dialog)
        self.setPlatformDir()
        self.buttonInit()
        
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "Blog 주소 :"))
        self.label_3.setText(_translate("Dialog", "https://"))
        self.label_4.setText(_translate("Dialog", ".tistory.com"))
        self.label_5.setText(_translate("Dialog", "Access Token :"))
        self.label_15.setText(_translate("Dialog", "문서 번호 :"))
        self.label_16.setText(_translate("Dialog", "   ~   "))
        self.label_17.setText(_translate("Dialog", "저장 위치 :  "))
        self.saveDirBtn.setText(_translate("Dialog", "..."))
        self.imageCheck.setText(_translate("Dialog", "Image 다운로드"))
        self.tagCheck.setText(_translate("Dialog", "Tag 포함 "))
        self.youtubeCheck.setText(_translate("Dialog", "Youtube"))
        self.settingBtn.setText(_translate("Dialog", "설정 완료"))
        self.stopBtn.setText(_translate("Dialog", "STOP"))
        self.startBtn.setText(_translate("Dialog", "START!"))

    def setPlatformDir(self):
        self.error_dialog = QtWidgets.QErrorMessage()
        if platform.system() == 'Windows':
            self.saveDir.setText(os.getcwd())
        elif platform.system() == 'Darwin':
            self.saveDir.setText(os.getcwd().split('tistory2md.app')[0])   

    def buttonInit(self):
        self.settingBtn.setEnabled(True)
        self.stopBtn.setEnabled(False)
        self.startBtn.setEnabled(False)

    def pushSettingBtn(self):
        self.stopBtn.setEnabled(True)
        self.startBtn.setEnabled(True)
        self.startBtn.setAutoDefault(True)

    def pushStartBtn(self):
        self.status.clear()
        self.stopBtn.setEnabled(True)
        self.startBtn.setEnabled(False)
        self.settingBtn.setEnabled(False)
        
    def openDir(self):
        fname = QFileDialog.getExistingDirectory(self, 'Open Folder', os.getcwd())
        self.saveDir.setText(fname)

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
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
