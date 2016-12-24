#coding=utf-8
import requests
import re
import json
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
url='http://www.ancc.org.cn/Service/queryTools/Internal.aspx#0'
my_headers={
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate,sdch',
   # 'Accept-Language':'zh-CN,zh;q=0.8',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    #'Content-Length':'504',
   # 'Content-Type':'application/x-www-form-urlencoded',
    'Host':'search.anccnet.com',
    #'Origin':'http://www.ancc.org.cn',
    'Referer':'http://www.ancc.org.cn/Service/queryTools/Internal.aspx',
    #'Upgrade-Insecure-Requests':'1'
}
r=requests.Session()
res=r.get(url)
resu=res.text
my_cookie=res.cookies
VIEWSTATE =re.findall(r'<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="(.*?)" />', resu,re.I)[0]
EVENTVALIDATION =re.findall(r'input type="hidden" name="__EVENTVALIDATION" id="__EVENTVALIDATION" value="(.*?)" />', resu,re.I)[0]
print VIEWSTATE
print EVENTVALIDATION
my_data={
    '__EVENTTARGET':'',
    '__EVENTARGUMENT':'',
    '__VIEWSTATE':VIEWSTATE,
    '__EVENTVALIDATION':EVENTVALIDATION,
    'Top%24h_keyword':'',
    'query-condition':'RadioItemInfo',
    'query-supplier-condition':'Radio1',
    'txtcode':'6954767413877',
    'btn_query':'%E6%9F%A5%E8%AF%A2+'
}
urll='http://www.ancc.org.cn/Service/queryTools/Internal.aspx'
#rrr=r.post(urll)
rrr=r.post(urll,data=my_data,headers=my_headers)
print rrr.url,rrr.status_code,rrr.history,rrr.text




# cur_url=responses.geturl()
# print cur_url
#print opener.open(req)

# try:
#     responses = opener.open(req)
#     result = responses.read().decode('gb2312')
#     # 由于该网页是gb2312的编码，所以需要解码
#     print result
#     # 打印登录后的页面
# except urllib2.HTTPError, e:
#     print e.code
# # result=opener.open(req)
# # a=result.read()
# # print a
# print VIEWSTATE[0]
# print EVENTVALIDATION[0]


