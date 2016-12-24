#coding:utf-8
import requests
import re
import sys
from lxml import etree
reload(sys)
sys.setdefaultencoding("utf-8")
file1=open("h.txt","r")
file2=open("zuihou3.csv","wb")
# he={
#     'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
#     'accept-encoding':'gzip, deflate, sdch, br',
#     'accept-language':'zh-CN,zh;q=0.8',
#     'cookie':'cna=Ve0QEM1ZU38CAXL/KDE7LJQy; _med=dw:1366&dh:768&pw:1366&ph:768&ist:0; sm4=110100; tt=tmall-main; _tb_token_=kxlTFV4LQSDI; ck1=; uc1=cookie14=UoWwJ08sJkc8uA%3D%3D&lng=zh_CN&cookie16=URm48syIJ1yk0MX2J7mAAEhTuw%3D%3D&existShop=false&cookie21=VT5L2FSpccLuJBreKQgf&tag=7&cookie15=U%2BGCWk%2F75gdr5Q%3D%3D&pas=0; uc3=sg2=BYLmQFqjdpQGU%2FRoyBdfVvuxqVX8xXrvk7IeNv%2FEwXk%3D&nk2=s0qR54e7PAXW90YP&id2=UU2w6wBwwLb2YQ%3D%3D&vt3=F8dAS1BplXhLGhheWRs%3D&lg2=URm48syIIVrSKA%3D%3D; lgc=%5Cu65B0%5Cu65B0%5Cu65B0%5Cu5B87%5Cu5B87%5Cu5B87; tracknick=%5Cu65B0%5Cu65B0%5Cu65B0%5Cu5B87%5Cu5B87%5Cu5B87; cookie2=cd90c677cd5ecad7e3f2a0b244a8184d; cookie1=WqVY7tI4tNBH8B40dWujnlUTMi04Yph22RqEFn5J2OA%3D; unb=2525049041; t=2d397b9de1e3200268a09bb0791bd30e; skt=a6c036dc3224f3d3; _nk_=%5Cu65B0%5Cu65B0%5Cu65B0%5Cu5B87%5Cu5B87%5Cu5B87; _l_g_=Ug%3D%3D; cookie17=UU2w6wBwwLb2YQ%3D%3D; hng=; uss=VqwcvPMgo65ZdlzRxZHEhSAMHgYNXA2WxCrwTqNGOgnI6wOVMUMrr3GWVA%3D%3D; login=true; cq=ccp%3D0; swfstore=164880; pnm_cku822=162UW5TcyMNYQwiAiwQRHhBfEF8QXtHcklnMWc%3D%7CUm5OcktxT3ZLf0B9RHBOey0%3D%7CU2xMHDJ7G2AHYg8hAS8XKwUlC1c2UDxbJV9xJ3E%3D%7CVGhXd1llXGZYYVxoV2pTZ1lsW2ZEekB7T3ZIckpwTHBJfURwT2E3%7CVWldfS0QMAUwCSkRMR98RWIYa0UTRQ%3D%3D%7CVmhIGCUFOBgkGiMXNw80AD0dIR8kHz8FPgsrFykSKQkzDDlvOQ%3D%3D%7CV25Tbk5zU2xMcEl1VWtTaUlwJg%3D%3D; res=scroll%3A1349*5690-client%3A1349*667-offset%3A1349*5690-screen%3A1366*768; otherx=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; whl=-1%260%260%260; x=__ll%3D-1%26_ato%3D0; l=Ap2dobk5K26LC1NXqzye9uMDLXOW99EM; isg=AhISyeKikX8IUu140T0IBgVPY9ijiBa9PmBuz9xqcEWw77HpxLHNzV1NKfyp',
#     'referer':'https://list.tmall.com/search_product.htm?q=%E7%8E%89%E7%B1%B3%E6%B2%B9',
#     'upgrade-insecure-requests':'1',
#     'user-agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
# }
line=file1.readline()
#count=0
while line :
    line=file1.readline()
 #   count=count+1
    for i in range(0,100):
        url='https://s.taobao.com/search?q='+line+'&s='+str(44*i)
        a=requests.get(url)
        a.encoding=("utf-8")
        r=re.findall('raw_title":"(.*?)"',a.text,re.S)
       # r.encode("utf-8")
        for each in r:
            file2.write(each)
            file2.write("^")
            file2.write(line)
            #file2.write("\n")
        num=0
        for each in r:
            print each
            num=num+1
        print num
file1.close()
file2.close()