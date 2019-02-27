# -*- coding: utf-8 -*-

"""
Module implementing Book_detial.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from Ui_book_detial import Ui_Dialog
from PyQt5.QtWidgets import QListWidgetItem
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import webbrowser
import cv2
from SqlOperator import SqlOperator

item=QListWidgetItem()
class Book_detial(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    #item=QListWidgetItem()
    def __init__(self, item):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        self.item=item
        super(Book_detial, self).__init__(parent=None)
        self.setupUi(self)
        self.sqlOperator = SqlOperator()
        
        self.setFixedSize(self.width(), self.height())
        
        self.book_pic(self.item)
        
    def book_pic(self, item):
        book_cover=str(item.whatsThis())
        book_cover=book_cover.replace('\\', '\\\\')
        result = self.sqlOperator.searchItem(book_cover)
        #print(result)
        
        book_cover_ = list(list(result)[0])[0]
        book_name = list(list(result)[0])[1]
        book_author = list(list(result)[0])[2]
        book_publish = list(list(result)[0])[3]
        book_introduction = list(list(result)[0])[5]
        book_number = list(list(result)[0])[6]
        book_location = list(list(result)[0])[10]
        
        #图书封面
        Im_cover = cv2.imread(book_cover_)  # 通过Opencv读入一张图片
        image_height, image_width= Im_cover.shape[:2]  # 获取图像的高，宽
        QIm_cover = cv2.cvtColor(Im_cover, cv2.COLOR_BGR2RGB)  # opencv读图片是BGR，qt显示要RGB，所以需要转换一下
        QIm_cover = QImage(QIm_cover.data, image_width, image_height, QImage.Format_RGB888)
        self.Cover_label.setScaledContents(True)#图片自适应大小
        self.Cover_label.setPixmap(QPixmap.fromImage(QIm_cover))  # 将QImage显示在之前创建的QLabel控件中
        #图书位置
        Im_location = cv2.imread(book_location)  # 通过Opencv读入一张图片
        image_height, image_width= Im_location.shape[:2]  # 获取图像的高，宽
        QIm_location = cv2.cvtColor(Im_location, cv2.COLOR_BGR2RGB)  # opencv读图片是BGR，qt显示要RGB，所以需要转换一下
        QIm_location = QImage(QIm_location.data, image_width, image_height, QImage.Format_RGB888)
        self.local_label.setScaledContents(True)#图片自适应大小
        self.local_label.setPixmap(QPixmap.fromImage(QIm_location)) 
        
        self.infor_textBrowser.append('书名：' + str(book_name))
        self.infor_textBrowser.append('作者：' + str(book_author))
        self.infor_textBrowser.append('出版社：' + str(book_publish))
        self.infor_textBrowser.append('书号：' + str(book_number))
        self.infor_textBrowser.append('图书简介：' + str(book_introduction))
    
    @pyqtSlot()
    def on_DD_pushButton_clicked(self):
        webbrowser.open('http://book.dangdang.com/?_utm_brand_id=11106&_ddclickunion=460-5-biaoti|ad_type=0|sys_id=1')
    
    @pyqtSlot()
    def on_JD_pushButton_clicked(self):
        webbrowser.open('https://book.jd.com/')
    
    @pyqtSlot()
    def on_DB_pushButton_clicked(self):
        webbrowser.open('https://book.douban.com/')
    
    @pyqtSlot()
    def on_Close_pushButton_clicked(self):
        self.close()
        

        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Book_detial(item)

    ui.show()
    sys.exit(app.exec_())
