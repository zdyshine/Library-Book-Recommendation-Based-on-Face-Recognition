# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
import sys
sys.path.append('./CustomTitlebar')   

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Ui_face_book import Ui_MainWindow
#import threadpool
#import time
#import threading
#import dlib
import cv2
from facecompare import Face
from SqlOperator import SqlOperator
from information import Information
from book_detial import Book_detial
from CameraThread import VideoThread
from RecomThread import RecomThread
import random
from PyQt5.QtGui import QImage


from Styles.CommonHelper import CommonHelper

class MainWindow(QMainWindow, Ui_MainWindow, QThread):
    """
    Class documentation goes here.
    """
    #PictureFrame = pyqtSignal(int)
    
    def book_detial_1(self, item):
        self.book_detial = Book_detial(item)
        self.__book_detial  = CommonHelper.FrameCustomerTitle(self.book_detial, "图书详情界面")
        self.__book_detial.move(160, 100)
        self.__book_detial.resize(850, 660)
        self.__book_detial.show()
    
    def __init__(self, parent=None,):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        #item1=None
        #导入外部定义的Class
        self.Face = Face()
        self.SqlOperator = SqlOperator()
        self.information = Information()
        self.cameraThread = VideoThread()
        self.recomThread = RecomThread()
        self.ret = ''
        
        self.num =''
        #self.major = ''
        #self.infor_img = []

#        self.git_thread = CloneThread()
        
        self.__information  = CommonHelper.FrameCustomerTitle(self.information, "信息采集界面")
        self.__information.move(160, 110)
        self.__information.resize(765, 443)
#        self.book_infor = Book_infor(self.item)
#        self.__book_infor  = CommonHelper.FrameCustomerTitle(self.book_infor, "图书详情界面")
#        self.__book_infor.move(160, 100)
#        self.__book_infor.resize(850, 660)

        self.QMessageBox = QtWidgets.QMessageBox()
        self.icon = QtGui.QIcon() #设置图标
        self.item = QtWidgets.QListWidgetItem()
        self.font = QtGui.QFont() #设置字体
        self.font.setPointSize(12)
        
        self.Logopic()#logo图片
        #显示时间
        timer = QTimer(self)
        timer.timeout.connect(self.showtime)
        timer.start()
        
#        self.openCamera.clicked.connect(self.OpenCamera)
#        self.cameraThread.VideoFrame.connect(self.Fresh_Video)#Video_Thread线程开启后捕捉摄像头调用Fresh_Video刷新界面
#        self.cameraThread.OpenVideoFlag.connect(self.Un_Open_Camera) #开启摄像头失败触发Un_Open_Camera函数

     
     #logo图片
    def Logopic(self): 
        Im = cv2.imread('D:\\Face_book\\logo.png')  # 通过Opencv读入一张图片
        image_height, image_width= Im.shape[:2]  # 获取图像的高，宽
        QIm = cv2.cvtColor(Im, cv2.COLOR_BGR2RGB)  # opencv读图片是BGR，qt显示要RGB，所以需要转换一下
        QIm = QImage(QIm.data, image_width, image_height, QImage.Format_RGB888)
        self.LogoLabel.setScaledContents(True)#图片自适应大小
        self.LogoLabel.setPixmap(QPixmap.fromImage(QIm))  # 将QImage显示在之前创建的QLabel控件中
        #视频区初始化图片
        self.CameraLabel.setScaledContents(True)#图片自适应大小
        self.CameraLabel.setPixmap(QPixmap.fromImage(QIm)) 
        
    #显示时间
    def showtime(self):
        now = QDate.currentDate()
        data = now.toString(Qt.DefaultLocaleLongDate)#2018年10月5日
        time_1 = QTime.currentTime()
        time_1 = time_1.toString(Qt.DefaultLocaleLongDate)#10:36:35
        self.time_label.setText(data  +  time_1)
        
#    def OpenCamera(self):
#        #打开摄像头
#        global t
#        #isopend=1
#        
#        self.cap = cv2.VideoCapture()
#        if (not self.cap.isOpened()):
#            self.cap.open(0)
#            self.cap.set(3, 500)
#            self.cap.set(4, 600)
#            #isopend=0
#        #self.PictureFrame.emit(isopend)
##        pool = threadpool.ThreadPool(10) 
##        requests = threadpool.makeRequests(self.Show_img, ())
##        [pool.putRequest(req) for req in requests] 
##        pool.wait() 
#        t =threading.Thread(target=self.Show_img,args=())
#        t.start()
#      
##        #获取当前帧图片
#    def Show_img(self):
#            while True:
#    #            QtCore.QCoreApplication.processEvents()
#                time.sleep(0.001)
#                self.ret,  self.imread_img = self.cap.read()
#                rert_1,  self.infor_img = self.cap.read()
#                if not self.ret:
#                    print('error: failed to capture image')
#                    return -1
#                 
#                self.detectorface()
#                
#                height, width= self.imread_img.shape[:2]
#                self.input_img = cv2.cvtColor(self.imread_img,  cv2.COLOR_BGR2RGB)
#                self.show_pic = QImage(self.input_img.data, width, height,  QImage.Format_RGB888)
#                self.CameraLabel.setScaledContents(True)#图片自适应大小
#                #self.label_show_camera.setGeometry(0, 0, 241, 211)#图片显示的位置（最左上角的点+大小）
#                 # 转为QImage对象
#                self.CameraLabel.setPixmap(QPixmap.fromImage(self.show_pic))
#
#    def detectorface(self):
#        self.detector = dlib.get_frontal_face_detector()
#        img_gray = cv2.cvtColor(self.imread_img, cv2.COLOR_RGB2GRAY)
#        faces = self.detector(img_gray, 0)
#       # faces = facecompare.Face.detect(self.input_img)
#        if (len(faces) != 0):
#            # for i in range(len(faces)):
#            for k, d in enumerate(faces):
#                # 用红色矩形框出人脸
#                cv2.rectangle(self.imread_img, (d.left(), d.top()), (d.right(), d.bottom()), (0, 0, 255), 3)

    def OpenCamera(self):
        if not self.cameraThread.isRunning():
            self.cameraThread.start()
            self.openCamera.setText("关闭摄像头")
        else:
            self.cameraThread.Stop_Video()
            self.Logopic()
        
    def Fresh_Video(self,show_pic):
        self.CameraLabel.setScaledContents(True)#图片自适应大小
        self.CameraLabel.setPixmap(QPixmap.fromImage(show_pic))
        
        #self.VideoLabel.setPixmap(QPixmap.fromImage(qImg))

    def Un_Open_Camera(self,bool):
        QtWidgets.QMessageBox.warning(self,"警告","打开摄像头失败")
        #self.openCamera.setText("打开摄像头")

    def start_recomThread(self):
        if not self.recomThread.start():
            self.recomThread.start()
    
    def start_gidentify(self):
        #self.recomThread.start()
        self.num, score= self.recomThread.gidentify()
        print(self.num)
        print(score)
        
        if(self.num ==-1 and score == -1):
            self.QMessageBox.warning(self, '警告', '未检测到人脸，请检查网络连接或靠近识别')
            return 0
            
        if(self.num != -1 and score > 0.80):
            result = self.recomThread.info_gidentify(self.num)#读取数据库信息
            #print(result)
            if result == None:
                self.QMessageBox.warning(self, '警告', '数据库可能没有您的数据或者靠近再次识别')
            else:
                self.Name_label.setText(result[2])
                self.Num_label.setText(result[3])
                self.Class_label.setText(result[5])
                self.Major_label.setText(result[4])
                self.love_recom(result[3])
                self.Class_recom(result[3])
                self.Major_recom(result[4])
                self.History(result[3])
                self.Hot_recom(result[3])
                self.Newbook_recom(result[3])
        else:
            self.QMessageBox.warning(self, '警告', '数据库可能没有您的数据或者检查网络连接再次识别')
            
#    def gidentify(self):
#        #cv2.imwrite("./recommend.jpg", self.imread_img)
#        self.num, score= self.Face.compare("./recommend.jpg")
#        #img = cv2.cvtColor(self.imread_img, cv2.COLOR_RGB2GRAY)
##        self.num, score= self.Face.compare(self.imread_img)
#        
#        print(self.num)
#        print(score)
#        
#        if(self.num ==-1 and score == -1):
#            self.QMessageBox.warning(self, '警告', '未检测到人脸，请检查网络连接或靠近识别')
#            return 0
#            
#        if(self.num != -1 and score > 0.80):
#            result = self.SqlOperator.searchbystunum(self.num)#读取数据库信息
#            if result == None:
#                self.QMessageBox.warning(self, '警告', '数据库可能没有您的数据或者靠近再次识别')
#            else:
#                self.Name_label.setText(result[2])
#                self.Num_label.setText(result[3])
#                self.Class_label.setText(result[5])
#                self.Major_label.setText(result[4])
#                self.love_recom(result[3])
#                self.Class_recom()
#                self.Major_recom(result[4])
#                self.History(result[3])
#                self.Hot_recom()
#                self.Newbook_recom()
#        else:
#            self.QMessageBox.warning(self, '警告', '请检查网络连接或者靠近再次识别')
   
    def Search_book(self):
        my_str = self.Search_line.text()
        if (my_str == ''):
            self.QMessageBox.information(self, '警告', '请输入搜索内容')
        else:
            #self.search_result = self.SqlOperator.search_by_name(str(my_str).strip())
            self.search_result = self.recomThread.Search_book(my_str)
            #print(self.search_result)
            for result in self.search_result:
                item = QtWidgets.QListWidgetItem(list(result)[1])
                self.icon.addPixmap(QtGui.QPixmap(list(result)[9]), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                item.setIcon(self.icon)
                self.Search_listWidget.setFont(self.font)
                item.setWhatsThis(list(result)[9])
                self.Search_listWidget.addItem(item)
#####################################

    #喜好推荐
    def love_recom(self, num):
#        lover_result_2=[]
#        lover_result = self.SqlOperator.search_lover_bystunum(str(num))
#        if lover_result != None:
#            lover_result_1=str(list(lover_result)[0]).split('|')
#        #print(1)
#            for  i in lover_result_1:
#                lover_result_2+=self.SqlOperator.searchdata(str(i))
#            lover_result_2=list(lover_result_2)
#            random.shuffle (lover_result_2)
#            #print(lover_result_2)
        lover_result_2 = self.recomThread.love_recom(num)
        random.shuffle (lover_result_2)
        
        if (lover_result_2 == None):
            self.favor_listWidget.addItem('暂无推荐')
        else:
            for result in lover_result_2[:9]:
                #print((list(result)[1]))
                item = QtWidgets.QListWidgetItem(list(result)[1])
                self.icon.addPixmap(QtGui.QPixmap(list(result)[9]), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                item.setIcon(self.icon)
                self.favor_listWidget.setFont(self.font)
                item.setWhatsThis(list(result)[9])
                self.favor_listWidget.addItem(item)
                
    #年级推荐           
    def Class_recom(self, num):
#        class_result=[]
#        self.class_listWidget.clear()
#        if self.num != -1:
#            class_result = self.SqlOperator.searchAll()
#            class_result=list(class_result)
#            random.shuffle (class_result)
        #print(lover_result_2)
        self.class_listWidget.clear()       
        class_result = self.recomThread.class_recom(num)
        random.shuffle (class_result)        
        if (class_result == None):
            self.class_listWidget.addItem('暂无推荐')
        else:
            for result in class_result[:9]:
                #print((list(result)[1]))
                item = QtWidgets.QListWidgetItem(list(result)[1])
                self.icon.addPixmap(QtGui.QPixmap(list(result)[9]), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                item.setIcon(self.icon)
                self.class_listWidget.setFont(self.font)
                item.setWhatsThis(list(result)[9])
                self.class_listWidget.addItem(item)
    #专业推荐
    def Major_recom(self, major):
#        major_result=[]
#        self.major_listWidget.clear()
#        major_result = self.SqlOperator.searchMajor(major)
#        major_result=list(major_result)
#        random.shuffle (major_result)
        self.major_listWidget.clear()
        major_result = self.recomThread.major_recom(major)
        random.shuffle (major_result)          
        if (major_result == None):
            self.major_listWidget.addItem('暂无借书记录')
        else:
            for result in major_result[:9]:
                #print((list(result)[1]))
                item = QtWidgets.QListWidgetItem(list(result)[1])
                self.icon.addPixmap(QtGui.QPixmap(list(result)[9]), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                item.setIcon(self.icon)
                self.major_listWidget.setFont(self.font)
                item.setWhatsThis(list(result)[9])
                self.major_listWidget.addItem(item)

    #历史记录           
    def History(self, num):
#        self.history_listWidget.clear()
#        self.history_result = self.SqlOperator.searchbynum(num)
        self.history_listWidget.clear()
        self.history_result = self.recomThread.history(num)
        if (self.history_result == None):
            self.history_listWidget.addItem('暂无借书记录')
        else:
            for result in self.history_result:
                item = QtWidgets.QListWidgetItem(list(result)[2])
                #icon = QtGui.QIcon()
                self.icon.addPixmap(QtGui.QPixmap(list(result)[1]), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                item.setIcon(self.icon)
                self.history_listWidget.setFont(self.font)
                item.setWhatsThis(list(result)[1])
                self.history_listWidget.addItem(item)
                
        
    #热门推荐
    def Hot_recom(self, num):
#        hot_result=[]
#        self.hot_listWidget.clear()
#        if self.num != -1:
#            hot_result = self.SqlOperator.searchAll()
#            hot_result=list(hot_result)
#            random.shuffle (hot_result)
#        #print(lover_result_2)
        self.hot_listWidget.clear()        
        hot_result = self.recomThread.hot_recom(num)
        random.shuffle (hot_result) 
        
        if (hot_result == None):
            self.hot_listWidget.addItem('暂无借书记录')
        else:
            for result in hot_result[:9]:
                #print((list(result)[1]))
                item = QtWidgets.QListWidgetItem(list(result)[1])
                self.icon.addPixmap(QtGui.QPixmap(list(result)[9]), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                item.setIcon(self.icon)
                self.hot_listWidget.setFont(self.font)
                item.setWhatsThis(list(result)[9])
                self.hot_listWidget.addItem(item)
                
    def Newbook_recom(self, num):
#        newbook_result=[]
#        self.Newbook_listWidget.clear()
#        if self.num != -1:
#            newbook_result = self.SqlOperator.searchAll()
#            newbook_result=list(newbook_result)
#            random.shuffle (newbook_result)
#        #print(lover_result_2)
        self.Newbook_listWidget.clear()        
        newbook_result= self.recomThread.newbook_recom(num)
        random.shuffle (newbook_result)         
        if (newbook_result == None):
            self.Newbook_listWidget.addItem('暂无借书记录')
        else:
            for result in newbook_result[:9]:
                #print((list(result)[1]))
                item = QtWidgets.QListWidgetItem(list(result)[1])
                self.icon.addPixmap(QtGui.QPixmap(list(result)[9]), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                item.setIcon(self.icon)
                self.Newbook_listWidget.setFont(self.font)
                item.setWhatsThis(list(result)[9])
                self.Newbook_listWidget.addItem(item)
                

   #打开摄像头
    @pyqtSlot()
    def on_openCamera_clicked(self):
#        self.git_thread.OpenCamera() #打开摄像头
#        self.git_thread.show_img()
#        #self.PictureFrame.connect(self.Show_img)
        self.OpenCamera() #打开摄像头
        self.cameraThread.VideoFrame.connect(self.Fresh_Video)#Video_Thread线程开启后捕捉摄像头调用Fresh_Video刷新界面
        self.cameraThread.OpenVideoFlag.connect(self.Un_Open_Camera) #开启摄像头失败触发Un_Open_Camera函数

    
    #进行识别 
    @pyqtSlot()
    def on_recommend_pushButton_clicked(self):
        #if not self.ret:
        if not self.cameraThread.isRunning():
            QMessageBox.information(self, '提示', '请先打开摄像头')
        else:
            #清空上次记录
            self.Name_label.clear()
            self.Num_label.clear()
            self.Class_label.clear()
            self.Major_label.clear()            
            #self.gidentify() #进行识别推荐
            self.start_recomThread()
            self.start_gidentify()

    #信息采集
    @pyqtSlot()
    def on_Info_pushButton_clicked(self):
        #if not self.ret:
        if not self.cameraThread.isRunning():
            print(not self.cameraThread.isRunning())
            QMessageBox.information(self, '提示', '请先打开摄像头')
        else:
            #cv2.imwrite("./infor.jpg", self.infor_img)
            self.information.Infor_img("./infor.jpg")
            self.__information.show()
        
     
     #图书搜索   
    @pyqtSlot()
    def on_Serach_pushButton_clicked(self):
        self.Search_listWidget.clear()
        self.Search_book()

    @pyqtSlot()
    def on_Clera_pushButton_clicked(self):
        self.Search_line.setText('')#清空
        
    @pyqtSlot(QListWidgetItem)
    def on_Search_listWidget_itemClicked(self, item):
       #self.__book_infor.show()
        self.book_detial_1(item)

    @pyqtSlot(QListWidgetItem)
    def on_favor_listWidget_itemClicked(self, item):
        #self.__book_infor.show()
        self.book_detial_1(item)

    @pyqtSlot(QListWidgetItem)
    def on_class_listWidget_itemClicked(self, item):
        #self.__book_infor.show()
        self.book_detial_1(item)

    @pyqtSlot(QListWidgetItem)
    def on_history_listWidget_itemClicked(self, item):
        #QMessageBox.information(self, '提示', '请选择其他版面点击')
        self.book_detial_1(item)
    
    @pyqtSlot(QListWidgetItem)
    def on_hot_listWidget_itemClicked(self, item):
        #self.__book_infor.show()
        self.book_detial_1(item)

   
    @pyqtSlot(QListWidgetItem)
    def on_major_listWidget_itemClicked(self, item): 
      #self.__book_infor.show()  
      self.book_detial_1(item)
      
    
    @pyqtSlot(QListWidgetItem)
    def on_Newbook_listWidget_itemClicked(self, item):
        self.book_detial_1(item)

  
  
if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    # 其他窗口调用方法也一样
    ui = MainWindow()
    framelessWindow = CommonHelper.FrameCustomerTitle(ui, "基于人脸识别的智能图书推荐系统")
    framelessWindow.move(50,10) #设置窗口初始化位置
    framelessWindow.resize(1000, 800) #设置窗口初始化大小
    framelessWindow.show()
    sys.exit(app.exec_())

