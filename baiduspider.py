# coding=utf-8
import httplib,urllib,requests
class search_baidu(object):
    def __init__(self, url):
        self.url = url
        self.request_header = {'User-Agen': "Mozilla/5.0 (Windows NT 6.1; rv:23.0) Gecko/20100101 Firefox/23.0",
                               'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                               'Accept-Language': "zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3",
                               'Accept-Encoding': "gzip, deflate",
                               'Referer': "http://www.baidu.com/",
                               'Cookie': "BAIDUID=79F58F8A7287106913C63CDA5BC1559B:FG=1; H_PS_PSSID=; BDSVRTM=0; WWW_ST=1377438509553",
                               'Connection': "keep-alive"
        }
        self.parameters = {'wd': "薄熙来",
                           'rsv_bp': "0",
                           'rsv_spt': "3",
                           'ie': "utf-8",
                           'rsv_sug3': "1",
                           'rsv_sug1': "1",
                           'rsv_sug4': "15",
                           'inputT': "10582"}

    def do_connect(self):
        try:
            self.conn = httplib.HTTPConnection(self.url)
            self.conn.request(method='GET', url = '/s?'+urllib.urlencode(self.parameters), headers=self.request_header)
            response = self.conn.getresponse()
            print response.read()
        except:
          if response.status == 302:
             print(response.read())
          else:
             print(response.read())
          self.conn.close()
