#encoding:utf-8
import urllib,urllib2,json,re
from time import sleep
from lxml import etree
pn=1
search_url=[]
headers = {'Host': 's.weibo.com',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2729.4 Safari/537.36',
           'Referer': 'http://s.weibo.com/user/&tag=%25E8%2580%2581%25E5%25B8%2588',
           'Cookie': 'SINAGLOBAL=1008552690978.3438.1463407377534; un=sly759@sina.com; wvr=6; _s_tentry=login.sina.com.cn; Apache=7517670557996.818.1463452077244; ULV=1463452077264:2:2:2:7517670557996.818.1463452077244:1463407377540; SWB=usrmdinst_22; WBStore=8ca40a3ef06ad7b2|undefined; UOR=www.wuleba.com,widget.weibo.com,www.liaoxuefeng.com; NSC_wjq_txfjcp_mjotij=ffffffff094113d545525d5f4f58455e445a4a423660; SUHB=0N2EOmQpR-Sela; ALF=1466045908; SUS=SID-1822822705-1463453908-XD-p8ylf-7ad34e3ae33e3029586daa5306f40dfa; SUE=es%3D51470ea071ac9f4e89ae9ab5bda7e6e4%26ev%3Dv1%26es2%3Ddb84e4d1008d86f4f3e13987e54e2929%26rs0%3DGEq9bglBQxiwGxOv%252FnU8457lETejveQ8QdiRsUsupGnlslE9RM%252B0u0JAt86d42kWb7QGr%252BFsai8u5%252FcVy5Vslsqtk%252FCkTpVf6BSrsucj6Hg04e3kKkU8RkIiHOmrvZv0uOMrftIg%252ByAPidIoj1PkD3YMObu6UiEZpa4ZrCczmBc%253D%26rv%3D0; SUP=cv%3D1%26bt%3D1463453908%26et%3D1463540308%26d%3Dc909%26i%3D0dfa%26us%3D1%26vf%3D%26vt%3D%26ac%3D%26st%3D0%26uid%3D1822822705%26name%3Dsly759%2540sina.com%26nick%3Dsly759%26fmp%3D%26lcp%3D2016-04-10%252010%253A14%253A59; SUB=_2A256PviEDeRxGedG6VAZ8izLyzmIHXVZwJjMrDV8PEJbuNM7aCGXkm5JbiPa0Tt0gMC8Ee6lu8OblxVSR00.; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5-xaSozIiGshlaw7J3cSXn5NHD95Qp1hzE1hzES05f; ULOGIN_IMG=14634578863158'
           }
uid1 = []
def uid(self):
    for pn in range(1,10):
        url='http://s.weibo.com/user/%25E8%2580%2581%25E5%25B8%2588&page='+str(pn)
        search_url.append(url)
        for i in  search_url:
            source=urllib2.Request(url,headers=headers)
            html = urllib2.urlopen(source).read()
            rex0=r'user_feed_\w+_name\\">\\n\\t(.*?)\\n\\t\\t\\n\\t<\\/a>'
            weibo_name = re.findall(rex0, html, re.S)
            rex1='uid=\\\\"(\d{10})'
            weibo_rawuid=re.findall(rex1,html,re.S)
            weibo_url=list(set(weibo_rawuid))
            uid1.extend(weibo_url)
        print 'graping uid sucess'
        sleep(3)
    return uid1

