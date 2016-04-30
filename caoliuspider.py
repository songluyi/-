import requests,urllib,urllib2,re
from multiprocessing.dummy import Pool as ThreadPool
class spider(object):
    def get_source(self,url):
        headers = {'Host':'cl.1024yq.info',
           'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36}',
           'Referer':'http://cl.1024yq.info/thread0806.php?fid=2',
           'Upgrade-Insecure-Requests':1,
           'cookies':'__cfduid=dd4d9f81e72cb289fa7f8135c941085f71461939432; CNZZDATA950900=cnzz_eid%3D1179136945-1461936069-http%253A%252F%252Fcl.1024yq.info%252F%26ntime%3D1461937405'
                 }
        html=urllib2.Request(url,headers = headers)
        response = urllib2.urlopen(html)
        text = response.read().decode('gbk')
        return text
    def get_everylink(self,source):
        everylink=re.findall('htm_data.*?html',source)
        all_link=[]
        for i in everylink:
            j='http://cl.1024yq.info/'+i
            all_link.append(j)
        return all_link
    def about_pic(self,source):
        p = re.compile(r'http://p2.*?.jpg')
        pic_url=re.findall(p,source)
        for i in pic_url:
            if len(i)>100:
                break
            else:
                img_name = re.sub(r'http://.*/','',i)
                path = 'E:\python learning\slylearnpython\yellowpic\heiheihei'+img_name
                urllib.urlretrieve(i,path)
    def get_everytitle(self,source):
        q = re.compile(r'<title>(.*?)</title>')
        every_title=re.findall(q,source)
        return every_title
if __name__=='__main__':
    pool = ThreadPool(4)
    caoliu=spider()
    for j in range(1,20):
        url='http://cl.1024yq.info/thread0806.php?fid=2&search=&page=%s' %j
        html=caoliu.get_source(url)
        all_links=caoliu.get_everylink(html)
        for i in all_links:
            print 'starting crawling %s link' %i
            source=caoliu.get_source(i)
            title=caoliu.get_everytitle(source)
            print(title[0])
            caoliu.about_pic(source)
    pool.close()
    pool.join()