# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Face_book\book_detial.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(855, 633)
        Dialog.setSizeGripEnabled(True)
        self.Close_pushButton = QtWidgets.QPushButton(Dialog)
        self.Close_pushButton.setGeometry(QtCore.QRect(740, 580, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Close_pushButton.setFont(font)
        self.Close_pushButton.setObjectName("Close_pushButton")
        self.DB_pushButton = QtWidgets.QPushButton(Dialog)
        self.DB_pushButton.setGeometry(QtCore.QRect(370, 580, 131, 41))
        self.DB_pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("DB.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.DB_pushButton.setIcon(icon)
        self.DB_pushButton.setIconSize(QtCore.QSize(127, 127))
        self.DB_pushButton.setObjectName("DB_pushButton")
        self.Cover_label = QtWidgets.QLabel(Dialog)
        self.Cover_label.setGeometry(QtCore.QRect(10, 10, 400, 560))
        self.Cover_label.setObjectName("Cover_label")
        self.JD_pushButton = QtWidgets.QPushButton(Dialog)
        self.JD_pushButton.setGeometry(QtCore.QRect(20, 582, 131, 41))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("JD.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.JD_pushButton.setIcon(icon1)
        self.JD_pushButton.setIconSize(QtCore.QSize(127, 127))
        self.JD_pushButton.setObjectName("JD_pushButton")
        self.DD_pushButton = QtWidgets.QPushButton(Dialog)
        self.DD_pushButton.setGeometry(QtCore.QRect(200, 580, 131, 41))
        self.DD_pushButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("DD.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.DD_pushButton.setIcon(icon2)
        self.DD_pushButton.setIconSize(QtCore.QSize(127, 127))
        self.DD_pushButton.setObjectName("DD_pushButton")
        self.infor_textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.infor_textBrowser.setGeometry(QtCore.QRect(410, 10, 431, 371))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.infor_textBrowser.setFont(font)
        self.infor_textBrowser.setObjectName("infor_textBrowser")
        self.local_label = QtWidgets.QLabel(Dialog)
        self.local_label.setGeometry(QtCore.QRect(410, 379, 431, 191))
        self.local_label.setObjectName("local_label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Close_pushButton.setText(_translate("Dialog", "返回"))
        self.Cover_label.setText(_translate("Dialog", "TextLabel"))
        self.local_label.setText(_translate("Dialog", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

