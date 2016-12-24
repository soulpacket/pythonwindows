#coding:utf-8
import zipfile
import re
ff=zipfile.ZipFile("channel.zip","r")
a=".txt"
f=1
d=["90052"]
comment=[]
#c=str(29)
while(d):
    e=d[0]
    b=open(e+a).read()
    comment.append(ff.getinfo(e+".txt").comment)
    print b
    d=re.findall("\d+",b)
   # comment.append(e)
print ''.join(comment)