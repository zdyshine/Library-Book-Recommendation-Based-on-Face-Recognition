# -*- coding: utf-8 -*-

"""
Module implementing Information.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


from Ui_information import Ui_Information

import cv2
import webbrowser
from SqlOperator import SqlOperator
from facecompare import Face
import sys

class Information(QMainWindow, Ui_Information):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Information, self).__init__(parent)
        self.setupUi(self)
        
        self.setFixedSize(self.width(), self.height())
        
        self.sqlOperator = SqlOperator()
        self.Face = Face()
        
        self.path = "D:\\\\Face_book\\\\infor.jpg"
        self.Infor_img(self.path)
        
    def Input_infor(self):
        lover = ''
        name = self.name_lineEdit.text()
        num = self.num_lineEdit.text()
        grade = self.grade_comboBox.currentText()
        major = self.major_comboBox.currentText()
        if (name == ''):
            QMessageBox.information(self, '警告', '请输入姓名')
        elif(num == ''):
            QMessageBox.information(self, '警告', '请输入学号')
        elif(grade == '——请选择年级——' ):
            QMessageBox.information(self, '警告', '请输入年级')
        elif(major == '——请选择专业——'):
            QMessageBox.information(self, '警告', '请输入专业')
        elif ((not self.checkBox.isChecked()) and (not self.checkBox_2.isChecked()) and (not self.checkBox_3.isChecked()) and (not self.checkBox_4.isChecked()) and (not self.checkBox_5.isChecked()) and (not self.checkBox_6.isChecked())):
            QMessageBox.information(self, '警告', '请选择一个喜好或选择其他')
        else:
            if (self.checkBox_4.isChecked()):
                if (lover == ''):
                    lover += '计算机科学与技术'
                else:
                    lover += "|计算机科学与技术"
            if (self.checkBox_2.isChecked()):
                if (lover == ''):
                    lover += '哲学'
                else:
                    lover += "|哲学"
            if (self.checkBox_3.isChecked()):
                if (lover == ''):
                    lover += '数学'
                else:
                    lover += "|数学"
            if (self.checkBox.isChecked()):
                if (lover == ''):
                    lover += '经济'
                else:
                    lover += "|经济"

            if (self.checkBox_5.isChecked()):
                if (lover == ''):
                    lover += '自动化'
                else:
                    lover += "|自动化"
            if (self.checkBox_6.isChecked()):
                if (lover == ''):
                    lover += '其他'
                else:
                    lover += "|其他"
        #print(lover)
            isSuccess = self.sqlOperator.insertFace(self.path, name, num, major, grade, lover)
            num_1 = self.Face.facecreate(self.path,num)
            print(num_1)
            if isSuccess :
                QMessageBox.information(self, '提示', '数据库添加成功')   
                
            if num_1 != -1:
                QMessageBox.information(self, '提示', '云端保存成功，请开始识别')
            else:
                QMessageBox.information(self, '提示', '网络延迟，请重新采集或后台手动添加')

    def Infor_img(self, img):
        self.Im = cv2.imread(img)  # 通过Opencv读入一张图片
        image_height, image_width= self.Im.shape[:2]  # 获取图像的高，宽
        QIm = cv2.cvtColor(self.Im, cv2.COLOR_BGR2RGB)  # opencv读图片是BGR，qt显示要RGB，所以需要转换一下
        QIm = QImage(QIm.data, image_width, image_height, QImage.Format_RGB888)
        self.Pic_label.setScaledContents(True)#图片自适应大小
        self.Pic_label.setPixmap(QPixmap.fromImage(QIm))  # 将QImage显示在之前创建的QLabel控件中
            
    @pyqtSlot()
    def on_Save_pushButton_clicked(self):
        self.Input_infor()

        self.name_lineEdit.clear()
        self.num_lineEdit.clear()
        self.grade_comboBox.clear()
        self.major_comboBox.clear()
#        self.checkBox.clear()
#        self.checkBox_2.clear()
#        self.checkBox_3.clear()
#        self.checkBox_4.clear()
    @pyqtSlot()
    def on_Close_pushButton_clicked(self):
        self.close()
      
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Information()
    ui.show()
    sys.exit(app.exec_())

