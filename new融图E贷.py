#-*_coding:utf8-*-
import urllib,httplib,requests,re
import urllib2,time
import json
from time import mktime
from datetime import datetime
from multiprocessing.dummy import Pool as ThreadPool
class spider(object):
    def __init__(self):
        print'starting crawing,please wait'
    def get_source(self,url):
        html = requests.get(url,headers=headers)
        return html.text
    def get_bidnum(self,source):
        bid_num=[]
        bid_link=re.findall('<a href="(.*?)" title="',source)
        for i in bid_link:
            i=i.replace('/invest/detail.html?borrowid=','')
            j=int(i)
            bid_num.append(j)
        return bid_num
    def get_bidlink(self,source):
        bidlink=[]
        bid_link=re.findall('<a href="(.*?)" title="',source)
        for i in bid_link:
            j='http://www.rongtudai.com/'+i
            bidlink.append(j)
        return bidlink
    def get_bidtitle(self,source):
        bid_info=re.findall('<a href=".*?" title="(.*?)">',source)
        return bid_info
    def get_investdate(self,source):
        q=re.compile('(.*?)<sub style="font-size: 16px; bottom:0px;">')
        date=re.findall(q,source)
        return date[1]
    def get_investrate(self,source):
        rate=re.findall('<b style="font-size: 30px; color: #f74747; margin-left: -20px;">(.*?)<sub style="font-size: 16px; bottom:0px;">%</sub></b>',source,re.S)
        return rate[0]
    def get_invest(self,url):
        s = requests.Session()
        info=s.request(method='GET',url = url, headers=headers,allow_redirects=False)
        return info.content
if __name__=='__main__':
    pool = ThreadPool(4)
    rongtuspider=spider()
    headers = {'Host':'www.rongtudai.com',
           'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0',
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'cookie':'footerHeight=235; Hm_lvt_5d54c74d98d62e4022542a84b015ccaf=1462317558,1462347708,1462347857,1462347866; jforumUserInfo=fucklogin; footerHeight=235; Hm_lpvt_5d54c74d98d62e4022542a84b015ccaf=1462366516; JSESSIONID=C7DF5A8EAB1C31934D28573FE07C179D',
           'Upgrade-Insecure-Requests':1,
           'Accept-Encoding':'gzip, deflate, sdch'
          }

    for a in range(1,6):
        url='http://www.rongtudai.com/invest/index.html?status=14&page=%s&sAccount=all&sLimit=all&search=union&sType=100&sApr=all&pageNum=10'%a
        print'正在爬第%s页'%a + url
        source=rongtuspider.get_source(url)
        bidlinks=rongtuspider.get_bidlink(source)
        title=rongtuspider.get_bidtitle(source)
        borrowid=rongtuspider.get_bidnum(source)
        i=0
        for every_title in title:
            bidsource=rongtuspider.get_source(bidlinks[i])
            invest_date=rongtuspider.get_investdate(bidsource)
            invest_date=invest_date.replace('\t','')
            invest_rate=rongtuspider.get_investrate(bidsource)
            id=int(borrowid[i])
            url='http://www.rongtudai.com/invest/detailTenderForJson.html?randID=Wed May 04 2016 20:55:16 GMT+0800&borrowid={0}&page=1'.format(id)
            invest_info=rongtuspider.get_invest(url)
            haha=eval(invest_info)
            count=len(haha['data']['list'])
            print '======================我是分割线========================'
            print 'Program name:'+every_title+' Invest data(month):'+str(invest_date)+'  Inest rate: '+str(invest_rate)+'%'
            for c in range(0,count):
                print '投资人：'+ haha['data']['list'][c]['username']
                print '投资金额:'+haha['data']['list'][c]['account']
                date=time.gmtime(float(haha['data']['list'][c]['addtime']))
                investtime=datetime.fromtimestamp(mktime(date))
                print '投资时间:'+ str(investtime)
        i+=1
    pool.close()
    pool.join()

