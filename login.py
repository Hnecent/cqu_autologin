# 本篇文档搬运至CSDN，原文链接：https://blog.csdn.net/weixin_40694662/article/details/128226508
# @author:runepic
# @date:20221207
# _*_ coding : utf-8 _*_

import re  # 正则表达式，用于匹配字符
import requests  # 用于向目标网站发送请求
import time
import socket
import datetime

schoolWebURL = "http://10.254.7.4/"

# 函数 gethostname() 返回当前正在执行 Python 的系统主机名
ip = socket.gethostbyname(socket.gethostname())
print(ip)

data = []
file = open("data.txt", 'r')  # 打开文件
file_data = file.readlines()  # 读取所有行
name = file_data[0].split(':')[1].replace('\n', '')
password = file_data[1].split(':')[1].replace('\n', '')
# tmp_list[-1] = tmp_list[-1].replace('\n',',') #去掉换行符
print(name)
print(password)

while (True):
    response = requests.get(schoolWebURL)
    # print(response)
    # 正则表达式，匹配<title>标签中的内容
    pattern = re.compile('<title>(.*?)</title>', re.S)
    title = re.findall(pattern, response.text)
    title = title[0]  # 将格式转为字符串
    print(title)

    if title == '注销页':  # 根据上面的分析填入相应的字符
        # print("保持登录，请不要关闭窗口...")
        time.sleep(60 * 60)
        pass
    else:
        # 使用GET方式登录校园网
        # 这行是你需要根据自己的情况修改的地方,不是重大的需要修改这一行
        schoolWebLoginURL = 'http://10.254.7.4:801/eportal/portal/login?callback=dr1004&login_method=1&user_account=%2C0%2C' + name + '&user_password=' + password + '&wlan_user_ip=' + ip + '&wlan_user_ipv6=2001%3Ada8%3Ac800%3Ad6b3%3Aacb0%3A5c66%3A6123%3A3294&wlan_user_mac=000000000000&wlan_ac_ip=&wlan_ac_name=&jsVersion=4.2&terminal_type=1&lang=zh-cn&v=1307&lang=zh'
        # requests.get(schoolWebLoginURL)
        response = requests.get(schoolWebLoginURL).status_code  # 直接利用 GET 方式请求这个 URL 同时获取状态码
        # print("状态码{}".format(response))  # 打印状态码
        if response == 200:
            print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "登录成功，请不要关闭窗口...")

    time.sleep(5)