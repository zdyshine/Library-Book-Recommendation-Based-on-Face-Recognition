#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : facecompare.py



import  base64, urllib, json
import http.client as httplib

APPID="user"
APPSECRET="12345"

class Face():
    def http_post(self,url, post):
        headers = {"Content-type": "application/x-www-form-urlencoded", 'Accept': "text/plain"}
        http = httplib.HTTPConnection("120.25.161.56", '8000',timeout=1)
        response = http.request('POST', url, post, headers)
        return http.getresponse().read().decode()

    def imgtobase64(self,img):
        with open(img,'rb') as imgf:
            try:
                imgdata = imgf.read()
                base64img = base64.b64encode(imgdata)
                return base64img
            except Exception as e:
                print (e)
#    def imgtobase64(self,img):
#
#        try:
#            base64img = base64.b64encode(img)
##            print(base64img)
#            return base64img
#        except Exception as e:
#            print (e)
                
    def facecreate(self, add_img,num):
        img = self.imgtobase64(add_img)
        post=urllib.parse.urlencode({'img':img})
        try:
            recv = self.http_post('/face/clustering/face/create?app_id='+APPID+'&app_secret='+APPSECRET+'&faceId=face_zdy&groupId=jxufe_zdy&tag='+str(num), post)
            resp = json.loads(recv)
    #            print(resp)
            resp['tag'] = num
            #print(resp['faceId'])
            print(resp['tag'])
    #           print(resp)
            sta =  int(resp.get('result', "-1"))
            if 0 == sta:
                print ("/face/clustering/face/create            \033[1;32m[Success]\033[0m")
            else:
                print ("/face/clustering/face/create            \033[1;31m[Faild]\033[0m")    
        except:
                    print ("Unknown error")
                    return -1
        return resp['tag']
 
 
    def compare(self,sourceimage):
        num=""
        score=0
        image=self.imgtobase64(sourceimage)
        post = urllib.parse.urlencode({'img': image})
        try:
            recv =self.http_post('/face/recog/group/identify?app_id=' + APPID + '&app_secret=' + APPSECRET + '&groupId=jx&topN=3',post)
            resp = json.loads(recv)
#            print(resp)
            num = resp['faces'][0].get('tag')
            score = resp['faces'][0].get('score')
#            print(score)
            sta = int(resp.get('result', "-1"))
    #           print(sta)
            if 0 == sta:
                print ("/face/recog/group/identify              \033[1;32m[Success]\033[0m")
            else:
                print ("/face/recog/group/identify              \033[1;31m[Faild]\033[0m")
        except:
            print ("Unknown error")
            return -1,-1
        #print('000000000' + num)
        return num ,score
