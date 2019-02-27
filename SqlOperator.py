#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymysql

class SqlOperator():
    def __init__(self):
        self.initdata()
    def initdata(self):
       self.conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='book', charset='utf8')
       # 通过cursor创建游标
       self.cursor = self.conn.cursor()

       
    def searchdata(self,type):
       # 执行数据查询
       sql = "SELECT * FROM book_all WHERE book_type=\'"+str(type)+"\'"
       self.cursor.execute(sql)
       
       #查询数据库多条数据
       result = self.cursor.fetchall()
#       print(result)
       return result
       
    def searchAll(self):
       # 执行数据查询
       sql = "SELECT * FROM book_all"
       self.cursor.execute(sql)
       
       #查询数据库多条数据
       result = self.cursor.fetchall()
#       print(result)
       return result
       
    def searchItem(self, item):
       # 执行数据查询
       #i='D:\\\\book_cover_1\\\\5\\\\18.png'
       sql = str("SELECT * FROM book_all WHERE book_cover_1=\'"+str(item)+"\'")
       #print(item)
       self.cursor.execute(sql)
       
       #查询数据库多条数据
       result = self.cursor.fetchall()
       #print(result)
       return result
       
    def searchMajor(self, major):
       # 执行数据查询
       sql = "SELECT * FROM book_all WHERE book_type=\'"+str(major)+"\'"
       self.cursor.execute(sql)
       
       #查询数据库多条数据
       result = self.cursor.fetchall()
#       print(result)
       return result
  
    def search_by_name(self, book_name):
       # 执行数据查询
       sql = "SELECT * FROM book_all WHERE book_name LIKE \'%"+str(book_name)+"%\'"
       self.cursor.execute(sql)
       
       #查询数据库多条数据
       result = self.cursor.fetchall()
#       print(result)
       return result  
   
#     def insertdata(self):
#         sql=""
#    def searchAll(self):
#        sql = "SELECT * FROM face_alll"
#        self.cursor.execute(sql)
#
#        # 查询数据库多条数据
#        result = self.cursor.fetchall()
#        return result

    def insertFace(self,photo,name,number,major,grade,lover):
       try:
        sql ="INSERT INTO face_all (photo,name, number,major,grade,lover) VALUES(\'"+photo+"\',\'"+name+"\',\'"+number+"\',\'"+major+"\',\'"+grade+"\',\'"+lover+"\')"
        #print(sql)
        self.cursor.execute(sql)
        self.conn.commit()
        return True
       except:
        print()
        # 发生错误时回滚
        self.conn.rollback()

    def searchbystunum(self,stunum):
        sql = "SELECT * FROM face_all WHERE number=\'"+stunum+"\'"
        self.cursor.execute(sql)

        # 查询数据库多条数据
        result = self.cursor.fetchone()
        return result
        
    def search_lover_bystunum(self,stunum):
            sql = "SELECT lover FROM face_all WHERE number=\'"+stunum+"\'"
            self.cursor.execute(sql)
    
            # 查询数据库多条数据
            result = self.cursor.fetchone()
            return result

    def searchbynum(self,num):
        sql = "SELECT * FROM book_record WHERE number=\'"+str(num)+"\'"
        self.cursor.execute(sql)

        # 查询数据库多条数据
        result = self.cursor.fetchall()
        return result
