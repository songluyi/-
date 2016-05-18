#-*-coding:utf8-*-
import re
import string
import sys
import os
import urllib
import urllib2
from bs4 import BeautifulSoup
import requests
from lxml import etree
reload(sys)
sys.setdefaultencoding('utf-8')
from teacheruid import uid
raw_uid=uid(self=None)
cookie = {"Cookie": "_T_WM=a798f2017c8332d62dfec205b7c8eb56; H5_INDEX=3; H5_INDEX_TITLE=sly759; M_WEIBOCN_PARAMS=uicode%3D20000173; SUB=_2A256PviDDeRxGedG6VAZ8izLyzmIHXVZwJjLrDV6PUJbrdBeLRCskW1LHetimTJuLNgp6_CZBJ_xmpp34G61vw..; SUHB=0103X0iuXXwbGP; SSOLoginState=1463453908"}
for user_id in raw_uid:
  int_uid=int(user_id)
  print 'starting graping %d'%int_uid
  url = 'http://weibo.cn/u/%d?filter=1&page=1'%int_uid
  html = requests.get(url, cookies = cookie).content
  selector = etree.HTML(html)
  pageNum = 10

  result = ""
  urllist_set = set()
  word_count = 1
  image_count = 1

  print u'爬虫准备就绪...'

  for page in range(1,pageNum+1):

  #获取lxml页面
    url = 'http://weibo.cn/u/%d?filter=1&page=%d'%(int_uid,page)
    lxml = requests.get(url, cookies = cookie).content

  #文字爬取
    selector = etree.HTML(lxml)
    content = selector.xpath('//span[@class="ctt"]')
    for each in content:
      text = each.xpath('string(.)')
      if word_count>=4:
        text = "%d :"%(word_count-3) +text+"\n \n "
      else :
        text = text+"\n \n"
      result = result + text
      word_count += 1
  fo = open("%s"%int_uid, "wb")
  fo.write(result)
  word_path=os.getcwd()+'/%d'%int_uid
  print u'微博账号：%d的文字微博爬取完毕'%int_uid
