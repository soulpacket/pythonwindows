#coding:utf-8
import urllib2
import requests
import cPickle as pickle
import pprint
file1=open("c.txt","wb")
#f=urllib2.urlopen('http://www.pythonchallenge.com/pc/def/banner.p')
f=requests.get('http://www.pythonchallenge.com/pc/def/banner.p')
#file1.write(f.text)
a=pickle.loads(str(f.text))
#result=pickle.Unpickler(file1).load()
#pprint.pprint(result)
#print type
#pprint.pprint(a)
for line in a:
    for c in line:
        file1.write(c[0]*c[1])
    file1.write('\n')
file1.close()