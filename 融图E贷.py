#-*_coding:utf8-*-
import urllib,cookielib
import urllib2
import json
import urllib
from pytesser import *
from PIL import Image
class spider(object):

    def get_code(self):
        url = 'http://www.rongtudai.com/validimg.html'
        f=urllib2.urlopen(url)
        with open("code.jpg", "wb") as code:
            code.write(f.read())
        img = Image.open('code.jpg')
        img = img.convert("RGBA")
        pixdata = img.load()
        for y in xrange(img.size[1]):
             for x in xrange(img.size[0]):
                if pixdata[x, y][0] < 90:
                    pixdata[x, y] = (0, 0, 0, 255)
        for y in xrange(img.size[1]):
            for x in xrange(img.size[0]):
                if pixdata[x, y][1] < 136:
                    pixdata[x, y] = (0, 0, 0, 255)
        for y in xrange(img.size[1]):
            for x in xrange(img.size[0]):
                if pixdata[x, y][2] > 0:
                    pixdata[x, y] = (255, 255, 255, 255)
        img.save('newcode.jpg')
        img = Image.open('newcode.jpg')
        vcode =image_to_string(img)
        return vcode
#下面这段是关键了，将为urlib2.urlopen绑定cookies
#MozillaCookieJar(也可以是 LWPCookieJar ，这里模拟火狐，所以用这个了) 提供可读写操作的cookie文件,存储cookie对象
cookiejar = cookielib.MozillaCookieJar()
# 将一个保存cookie对象，和一个HTTP的cookie的处理器绑定
cookieSupport= urllib2.HTTPCookieProcessor(cookiejar)
#下面两行为了调试的
httpHandler = urllib2.HTTPHandler(debuglevel=1)
httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
#创建一个opener，将保存了cookie的http处理器，还有设置一个handler用于处理http的
opener = urllib2.build_opener(cookieSupport, httpsHandler)
#将包含了cookie、http处理器、http的handler的资源和urllib2对象绑定在一起，安装opener,此后调用urlopen()时都会使用安装过的opener对象，
urllib2.install_opener(opener)
##提取验证码text(手动输入验证码)
#登陆页面
loginpage = "http://www.rongtudai.com/user/login.html"
#要post的url
PostUrl = "http://www.rongtudai.com/user/doLogin.html"
#打开登陆页面, 以此来获取cookies   。  但是因为  ##打开验证码页面就可以获取全部cookies了，所以可以直接跳过这一步。算是可有可无的
LoginCookies = urllib2.urlopen(loginpage)
#打印cookies
print  	cookiejar
#先打开页面获取的cookie与  后打开验证码页面的cookie不同。




rongtu=spider()
loginpage = 'http://www.rongtudai.com/user/login.html'
url = 'http://www.rongtudai.com/user/doLogin.html'
headers = {'Host':'www.rongtudai.com',
           'Origin':'http://www.rongtudai.com',
           'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36}',
           'Referer':'http://www.rongtudai.com/user/login.html',
           'Upgrade-Insecure-Requests':1,
           'X-Requested-With':'XMLHttpRequest',
           'cookies':'footerHeight=235; JSESSIONID=DB234EE097A31D54AE9DA772A5B7C1EB; footerHeight=235; Hm_lvt_5d54c74d98d62e4022542a84b015ccaf=1461751340; Hm_lpvt_5d54c74d98d62e4022542a84b015ccaf=1461754866'
          }
data ={'username':'fucklogin',
       'password':'fuck123321',
       'valicode':int(rongtu.get_code()),
       'actionType':'login',
       }
data=urllib.urlencode(data)
wb_data = urllib2.Request(url, headers = headers ,data = data)
response = urllib2.urlopen(wb_data)
text = response.read()
print text