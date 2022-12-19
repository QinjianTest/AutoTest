import requests
from utils.LogUtil import my_log
#1、创建封装get方法
def requests_get(url,headers):
#2、发送requests get请求
    r = requests.get(url,headers = headers)
#3、获取结果相应内容
    code = r.status_code
    try:
        body = r.json()
    except Exception as e:
        body = r.text
#4、内容存到字典
    res = dict()
    res["code"] = code
    res["body"] = body
#5、字典返回
    return res

#post方法封装
#1、创建post方法
def requests_post(url,json=None,headers=None):
#2、发送post请求
    r= requests.post(url,json=json,headers=headers)
#3、获取结果内容
    code = r.status_code
    try:
        body = r.json()
    except Exception as e:
        body = r.text
#4、内容存到字典
    res = dict()
    res["code"] = code
    res["body"] = body
#5、字典返回
    return res

#重构
#1、创建类
class Request:
#2、定义公共方法
    def __init__(self):
        self.log = my_log("Requests")
    def requests_api(self,url,data = None,json=None,headers=None,cookies=None,method="get"):

        if method =="get":
            #get请求
            self.log.debug("发送get请求")
            r = requests.get(url, data = data, json=json, headers=headers,cookies=cookies)
        elif method == "post":
            #post请求
            self.log.debug("发送post请求")
            r = requests.post(url,data = data,  json=json, headers=headers,cookies=cookies)

        #2. 重复的内容，复制进来
        #获取结果内容
        code = r.status_code
        try:
            body = r.json()
        except Exception as e:
            body = r.text
        #内容存到字典
        res = dict()
        res["code"] = code
        res["body"] = body
        #字典返回
        return res

#3、重构get/post方法
    #get
    #1、定义方法
    def get(self,url,**kwargs):
    #2、定义参数
        #url,json,headers,cookies,method
    #3、调用公共方法
        return self.requests_api(url,method="get",**kwargs)

    def post(self,url,**kwargs):
    #2、定义参数
        #url,json,headers,cookies,method
    #3、调用公共方法
        return self.requests_api(url,method="post",**kwargs)