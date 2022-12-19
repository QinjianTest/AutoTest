#1、导入requests包
import requests
#2、发送get请求
r = requests.get("http://www.baidu.com")
#3、打印结果
print(r.status_code)
print(r.headers)
# print(r.json())
print(r.url)
print(r.cookies)
print(r.text)

