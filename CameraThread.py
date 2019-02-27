from Ui_face_book import Ui_MainWindow
from PyQt5.QtCore import *
import cv2
import numpy 
from PyQt5.QtGui import QImage
from PyQt5.QtCore import QThread
import dlib
import time

class VideoThread(QThread,Ui_MainWindow):
    
    VideoFrame = pyqtSignal(QImage)
    OpenVideoFlag = pyqtSignal (bool)
    
    OpenInfoThread = pyqtSignal(list,numpy.ndarray)

    def __init__(self):
        super().__init__()

    def run(self):
        #打开摄像头
        self.Run_Video_Flag = 1
        self.cap = cv2.VideoCapture(0)
        
        if (not self.cap.isOpened()):
            self.cap.open()
            self.cap.set(3, 500)
            self.cap.set(4, 600)
            
        elif (self.cap.isOpened()):
            while self.Run_Video_Flag:
                ret,  img_read = self.cap.read()
                #print('11111111111')
                cv2.imwrite("./recommend.jpg", img_read)
                cv2.imwrite("./infor.jpg", img_read)
                
                if ret:
                    self.detectorface(img_read)#画框
                    
                    height, width= img_read.shape[:2]
                    input_img = cv2.cvtColor(img_read,  cv2.COLOR_BGR2RGB)
                    show_pic = QImage(input_img.data, width, height,  QImage.Format_RGB888)                    
                    if self.Run_Video_Flag:
                        self.VideoFrame.emit(show_pic)
                    else:
                        break
                    time.sleep(0.001) 
                else:
                    print("摄像头已打开，但无法read帧")
                    
            self.cap.release()
            self.quit()       
        else:
            self.OpenVideoFlag.emit(self.cap.isOpened())

            
    def detectorface(self, img):
        detector = dlib.get_frontal_face_detector()
        img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        faces = detector(img_gray, 0)
       # faces = facecompare.Face.detect(self.input_img)
        if (len(faces) != 0):
            # for i in range(len(faces)):
            for k, d in enumerate(faces):
                # 用红色矩形框出人脸
                cv2.rectangle(img, (d.left(), d.top()), (d.right(), d.bottom()), (0, 0, 255), 3)
    
    def Stop_Video(self):        
        self.Run_Video_Flag = 0

