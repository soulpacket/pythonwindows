#coding:utf-8
import requests
import sys
import random
from lxml import etree
import time
reload(sys)
sys.setdefaultencoding("utf-8")
import re
file1=open("mobankongmc.txt","wb")
file2=open("mobankong.txt","r")
line=file2.readline()
#num=1
while line:
    line=file2.readline()
    print line
    if line:
        uuu='http://www.ancc.org.cn/Service/queryTools/Internal.aspx#0'
       # my_cookie=requests.get(uuu).cookies
        url='http://search.anccnet.com/searchResult2.aspx?keyword='+str(line)
        my_headers={
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding':'gzip, deflate, sdch',
            #'Accept-Language':'zh-CN,zh;q=0.8',
           # 'Cookie':my_cookie,
            'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
            'Cache-Control':'max-age=0',
            'Connection':'keep-alive',
            'Host':'search.anccnet.com',
            'Referer':'http://www.ancc.org.cn/Service/queryTools/Internal.aspx',
            #'Upgrade-Insecure-Requests':'1'
        }
       # rrr=requests.Session()
        r=requests.get(url,headers=my_headers)
        time.sleep(8+random.random())
        #r.encoding=('utf-8')
        #print r.text
        selector=etree.HTML(r.text)
        content=selector.xpath('//*[@id="results"]/li/div/dl[1]/dd[1]/text()')
        content1=selector.xpath('//*[@id="results"]/li/div/dl[2]/dd[2]/text()')
        content2=selector.xpath('//*[@id="results"]/li/div/dl[2]/dd[3]/text()')
        #print r.cookies
        print content,content1
        if content:
            file1.write(content[0])
            file1.write(content1[0])
            file1.write(content2[0])
            file1.write("\n")
        elif ((not content)and content1) :
            file1.write(content1[0])
            file1.write("\n")
        else:
            file1.write("\n")
    else:
        file1.write("\n")
file1.close()
file2.close()