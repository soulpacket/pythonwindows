#coding:utf-8
import requests
import re
from lxml import etree
hea = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36'}
file1=open("lei.txt","r")
line=file1.readline()
print line
while line:
    line=file1.readline()
    print line
    url='https://list.tmall.com/search_product.htm?q='+line
    a=requests.get(url,headers=hea)
    print a.text
   # r=re.findall('blank" title="(.*?)" data',a.text,re.S)
    #print r
    #selector=etree.HTML(a.text)
    #//*[@id="J_ItemList"]/div[3]/div/p[2]/a
    #content=selector.xpath('//*[@id="J_ItemList"]/div[2]/div/p[2]/a')
#    print content
#file1.close()
# a= u'米'.encode('gbk')
# print len(a)
# url='https://list.tmall.com/search_product.htm?q=%D3%F1%C3%D7%D3%CD&type=p&vmarket=&spm=875.7931836%2FA.a2227oh.d100&from=mallfp..pc_1_searchbutton'
# a=requests.get(url)
# print a.text
