# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\86181\Desktop\t3\idiom_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(541, 401)
        self.lblIdiom = QtWidgets.QLabel(Form)
        self.lblIdiom.setGeometry(QtCore.QRect(10, 46, 181, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblIdiom.sizePolicy().hasHeightForWidth())
        self.lblIdiom.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lblIdiom.setFont(font)
        self.lblIdiom.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.lblIdiom.setObjectName("lblIdiom")
        self.lblName1 = QtWidgets.QLabel(Form)
        self.lblName1.setGeometry(QtCore.QRect(10, 98, 57, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lblName1.setFont(font)
        self.lblName1.setObjectName("lblName1")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(10, 140, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.lblName2 = QtWidgets.QLabel(Form)
        self.lblName2.setGeometry(QtCore.QRect(270, 10, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lblName2.setFont(font)
        self.lblName2.setObjectName("lblName2")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(280, 40, 211, 331))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(70, 220, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.cancelButton = QtWidgets.QPushButton(Form)
        self.cancelButton.setGeometry(QtCore.QRect(70, 270, 71, 31))
        self.cancelButton.setMinimumSize(QtCore.QSize(0, 27))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cancelButton.setFont(font)
        self.cancelButton.setObjectName("cancelButton")
        self.lblName1_2 = QtWidgets.QLabel(Form)
        self.lblName1_2.setGeometry(QtCore.QRect(10, 8, 57, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lblName1_2.setFont(font)
        self.lblName1_2.setObjectName("lblName1_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "成语接龙"))
        self.lblIdiom.setText(_translate("Form", "成语"))
        self.lblName1.setText(_translate("Form", "接龙："))
        self.lineEdit.setText(_translate("Form", "成语"))
        self.lblName2.setText(_translate("Form", "PK记录："))
        self.pushButton.setText(_translate("Form", "回答"))
        self.cancelButton.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">放弃</span></p></body></html>"))
        self.cancelButton.setText(_translate("Form", "放弃"))
        self.lblName1_2.setText(_translate("Form", "出题："))

