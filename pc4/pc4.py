#coding:utf-8
import requests
import re
a='http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
b='http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345'
e=[]
for i in range(0,400):
    c=requests.get(b)
    print i,c.text
    if(c.text[0]=='a'):
        d=re.findall("and the next nothing is (\d+)", c.text,re.S)[0]
        b=a+d
        e.append(d)
       # print d
    elif(c.text[0]=='Y'):
        f=int(e[i-1])/2
        print f
        e.append(str(f))
        b=a+str(f)
    if(c.text[0]=='<'):
        d=re.findall("and the next nothing is (\d+)", c.text,re.S)[0]
        b=a+d
        e.append(d)
    if(c.text[0]=='T'):
        d=re.findall("and the next nothing is (\d+)", c.text,re.S)[0]
        b=a+d
        e.append(d)


