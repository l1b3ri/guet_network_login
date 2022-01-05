# -*- coding: utf-8 -*-
import os
import socket

def login():
    os.system("curl -i -s -k -X $'GET' \
        -H $'Host: 10.0.1.5:801' -H $'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36' -H $'Accept: */*' -H $'Referer: http://10.0.1.5/' -H $'Accept-Encoding: gzip, deflate' -H $'Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7' -H $'Connection: keep-alive' \
        $'http://10.0.1.5:801/eportal/portal/login?callback=dr1003&login_method=<登录方式>&user_account=,0,<学号>@cmcc&user_password=<密码>&wlan_user_ip=&wlan_user_ipv6=&wlan_user_mac=000000000000&wlan_ac_ip=&wlan_ac_name=&jsVersion=4.1&terminal_type=1&lang=zh-cn&v=5021&lang=zh'")

def isNetOK(testserver):
    s=socket.socket()
    s.settimeout(3)
    try:
        status = s.connect_ex(testserver)
        if status == 0:
            s.close()
            return True
        else:
            return False
    except Exception as e:
        return False

def isNetChainOK(testserver=('www.baidu.com',443)):
    isOK = isNetOK(testserver)
    return isOK

if __name__ == '__main__':
    login()
    chinanet = isNetChainOK()
    if(chinanet == True):
        print("成功连接校园网")
    else:
        print("连接失败")

