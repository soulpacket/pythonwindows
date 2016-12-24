#coding:utf-8
from __future__ import division
import requests
import re
import math
# r=requests.get('http://www.xiami.com/space/lib-artist/u/108613?spm=a1z1s.6928797.1561534513.3.DMIS2Q')
# a=r.text
# print a
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
#hea是我们自己构造的一个字典，里面保存了user-agent。
#让目标网站误以为本程序是浏览器，并非爬虫。
#从网站的Requests Header中获取。【审查元素】
hea = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36'}
#f=open("dataset","r")
#file1=open("data.txt","wb")
file2=open("12345.csv","wb")
file3=open("testfile.txt","r")
line = file3.readline()             # 调用文件的 readline()方法
d=1
while line:
    print line,    # 后面跟 ',' 将忽略换行符
    file2.write(str(d))
    file2.write("\n")
    d=d+1
    # print(line, end = '')　　　# 在 Python 3中使用
    line = file3.readline()
    web1=re.findall('u/(.*?)\?spm',line,re.S)[0]
    print web1
    c='http://www.xiami.com/space/lib-album/u/'+web1
    content1=requests.get(c,headers=hea)
#    content1.encoding='utf-8'
    numa=re.findall('counts">(.*?)</span>',content1.text,re.S)[0]#字符串61条
    num1=len(numa)-1#得到数字的个数
    #print num1
    totalnum=0
    for num2 in range(0,num1):
        totalnum=totalnum+int(numa[num2])*(10**(num1-1-num2))#得到总条数
    print totalnum
    floatpagenum=math.ceil(totalnum/15)
    pagenum=int(floatpagenum)
    print pagenum
    for num in range(1,pagenum+1):
        b='http://www.xiami.com/space/lib-album/u/'+web1+'/page/'+str(num)
        html=requests.get(b, headers=hea)
        website=re.findall('href="/artist/(.*?)"',html.text,re.S)
        for each in website:
            # print 'http://www.xiami.com'+each
            a='http://www.xiami.com/artist/'+each
            print a
            r=requests.get(a, headers=hea)
            r.encoding = 'utf-8' #这一行是将编码转为utf-8否则中文会显示乱码。
     #   print r.text r.text代表网站的html源码
 #           file1.write(r.text)#把每个musician网站信息html输入到data.text中
            res = re.findall('<div id="page"(.*?)<div class="record"',r.text,re.S)
            if len(res)!=0:
        #    print len(res)
                thesecond=res[0]
                second=re.findall('rel="nofollow">(.*?)</a>',thesecond,re.S)
                name=re.search('<h1>(.*?)<span>',r.text,re.S).group(1)
                state=re.search('<td valign="top">(.*?)</td>',r.text,re.S).group(1)
                for every in second:
                    file2.write(every)
                    file2.write(",")
                    file2.write(name)
                    file2.write(",")
                    file2.write(state)
                    file2.write("\n")
#file1.close()
file2.close()
file3.close()



