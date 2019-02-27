from Ui_face_book import Ui_MainWindow
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QListWidget
from facecompare import Face
from SqlOperator import SqlOperator


class RecomThread(QThread,Ui_MainWindow ):
    
    BookWidget = pyqtSignal(QListWidget)
    recom_signal = pyqtSignal(int, int)
    
    def __init__(self):
        super().__init__()
        
        self.Face = Face()
        self.SqlOperator = SqlOperator()

    def gidentify(self):
        num, score= self.Face.compare("./recommend.jpg")
        self.recom_signal.emit(num, score)
        return num, score
        
    def info_gidentify(self, num):
            result = self.SqlOperator.searchbystunum(num)#读取数据库信息                       
            return  result       
        
    def Search_book(self, my_str):
        search_result = self.SqlOperator.search_by_name(str(my_str).strip())
        return search_result
        
    #喜好推荐
    def love_recom(self, num):
        lover_result_2=[]
        lover_result = self.SqlOperator.search_lover_bystunum(str(num))
        if lover_result != None:
            lover_result_1=str(list(lover_result)[0]).split('|')
            for  i in lover_result_1:
                lover_result_2+=self.SqlOperator.searchdata(str(i))
            lover_result_2=list(lover_result_2)            
        return lover_result_2   
        
    #年级推荐           
    def class_recom(self, num):
        class_result=[]
        if num != -1:
            class_result = self.SqlOperator.searchAll()
            class_result=list(class_result)
        return class_result
        
    #专业推荐
    def major_recom(self, major):
        major_result=[]
        major_result = self.SqlOperator.searchMajor(major)
        major_result=list(major_result)
        return major_result
   
    #历史记录           
    def history(self, num):
        self.history_result = self.SqlOperator.searchbynum(num)
        return self.history_result
                
        
    #热门推荐
    def hot_recom(self, num):
        hot_result=[]
        if num != -1:
            hot_result = self.SqlOperator.searchAll()
            hot_result=list(hot_result)
            
        return hot_result
                
    def newbook_recom(self, num):
        newbook_result=[]

        if num != -1:
            newbook_result = self.SqlOperator.searchAll()
            newbook_result=list(newbook_result)
        return newbook_result
