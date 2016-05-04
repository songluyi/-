#-*-coding:utf-8-*-
import httplib,urllib;  #加载模块
params = urllib.urlencode({'cat_id':'6',
                           'news_title':'标题-Test39875',
                           'news_author':'Mobedu',
                           'news_ahome':'来源',
                           'tjuser':'carchanging',
                           'news_keyword':'|',
                           'news_content':'测试-Content',
                           'action':'newnew',
                           'MM_insert':'true'});
#定义一些文件头
headers = {"Content-Type":"application/x-www-form-urlencoded",
           "Connection":"Keep-Alive","Referer":"http://192.168.1.212/newsadd.asp?action=newnew"};
#与网站构建一个连接
conn = httplib.HTTPConnection("192.168.1.212");
#开始进行数据提交   同时也可以使用get进行
conn.request(method="POST",url="/newsadd.asp?action=newnew",body=params,headers=headers);
#返回处理后的数据
response = conn.getresponse();
#判断是否提交成功
if response.status == 302:
    print "发布成功!^_^!";
else:
    print "发布失败\^0^/";
#关闭连接
conn.close();
