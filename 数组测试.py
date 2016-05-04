__author__ = 'Administrator'
import json,time
from time import mktime
from datetime import datetime
a={"data":{"list":[{"account":"8000.000000","addtime":"1461807846","auto_repurchase":0,"award_after_push":0,"borrow_account":0,"borrow_id":0,"hongbao":0,"id":0,"is_auto_tender":0,"money":"8000.000000","site_id":0,"status":1,"user_id":0,"username":"278866***"},{"account":"8000.000000","addtime":"1461907962","auto_repurchase":0,"award_after_push":0,"borrow_account":0,"borrow_id":0,"hongbao":0,"id":0,"is_auto_tender":0,"money":"8000.000000","site_id":0,"status":1,"user_id":0,"username":"nizhen***"},{"account":"6000.000000","addtime":"1462242604","auto_repurchase":0,"award_after_push":0,"borrow_account":0,"borrow_id":0,"hongbao":0,"id":0,"is_auto_tender":0,"money":"6000.000000","site_id":0,"status":1,"user_id":0,"username":"464135***"},{"account":"8000.000000","addtime":"1462242637","auto_repurchase":0,"award_after_push":0,"borrow_account":0,"borrow_id":0,"hongbao":0,"id":0,"is_auto_tender":0,"money":"8000.000000","site_id":0,"status":1,"user_id":0,"username":"1600448***"}],"page":{"currentPage":1,"end":4,"pages":1,"pernum":10,"start":0,"total":4},"type":0},"msg":"success"}

print len(a['data']['list'])
for i in range(0,len(a['data']['list'])):
     print a['data']['list'][i]['username']
     print a['data']['list'][i]['account']


b={"data":{"list":[{"account":"8000.000000","addtime":"1461807846","auto_repurchase":0,"award_after_push":0,"borrow_account":0,"borrow_id":0,"hongbao":0,"id":0,"is_auto_tender":0,"money":"8000.000000","site_id":0,"status":1,"user_id":0,"username":"278866***"},{"account":"8000.000000","addtime":"1461907962","auto_repurchase":0,"award_after_push":0,"borrow_account":0,"borrow_id":0,"hongbao":0,"id":0,"is_auto_tender":0,"money":"8000.000000","site_id":0,"status":1,"user_id":0,"username":"nizhen***"},{"account":"6000.000000","addtime":"1462242604","auto_repurchase":0,"award_after_push":0,"borrow_account":0,"borrow_id":0,"hongbao":0,"id":0,"is_auto_tender":0,"money":"6000.000000","site_id":0,"status":1,"user_id":0,"username":"464135***"},{"account":"8000.000000","addtime":"1462242637","auto_repurchase":0,"award_after_push":0,"borrow_account":0,"borrow_id":0,"hongbao":0,"id":0,"is_auto_tender":0,"money":"8000.000000","site_id":0,"status":1,"user_id":0,"username":"1600448***"}],"page":{"currentPage":1,"end":4,"pages":1,"pernum":10,"start":0,"total":4},"type":0},"msg":"success"}
print len(b['data']['list'])
print b['data']['list']
c=time.gmtime(float(b['data']['list'][1]['addtime']))
print c
d=type(c)
dt = datetime.fromtimestamp(mktime(c))
print time.gmtime(1461807846)
