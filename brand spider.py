# -*- coding: utf-8 -*-
# 2016/6/22 22:56
"""
-------------------------------------------------------------------------------
Function:
Version:    1.0
Author:     SLY
Contact:    slysly759@gmail.com 
 
-------------------------------------------------------------------------------
"""
import urllib2,urllib
keyword=raw_input('please input your keyword:')
url='http://www.chatm.com/chatm/multipleCategoryJson'
data = urllib.urlencode({'curPage':"2",
                           'isPageNum':"true",
                           'isPageInit':"true",
                           'status':"-1",
                           'keyword':keyword,
                           'ganre':"计算机端设备",
                           'operatingSystem':"Win7",
                           'browser':"FF",
                           'screenPint':"1366+*+768",
                           'cip':"171.34.163.251",
                           'cname':"国内未能识别的地区",
                           'url':"/chatm/multipleCategoryJson",
                           'category':"全部",
                           'token':"2016062310511447641682"});
headers = {'Host': 'www.chatm.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',
            'Referer': 'http://www.chatm.com/chatm/getList?keywords=%E4%BC%98%E8%A1%A3%E5%BA%93',
            'Content-Length':372,
            'Cookie': 'chatmuid=0b7a25d2-4337-40a7-a38c-e84b673b19ae; Hm_lvt_eb194d5472c74b4fef24b33d4106dd2c=1466606659,1466650077; sid=fce4248c-e0e8-4889-82f2-7b0fdef52547; Hm_lpvt_eb194d5472c74b4fef24b33d4106dd2c=1466650106; JSESSIONID=C640E3215F57DDA6DD95BFB5887362BC.tomcat12',
            'Connection': 'keep-alive'}

req = urllib2.Request(url, data, headers)
response = urllib2.urlopen(req)
the_page = response.read()

print the_page