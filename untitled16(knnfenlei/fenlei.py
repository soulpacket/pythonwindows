#coding:utf-8
import numpy as np
import operator
file1=open("mc.txt","r")
file2=open("fenlei.txt","r")
file3=open("spmc.txt","r")
file4=open("outcome.txt","wb")
list_mc=[]
line_mc=file1.readline()
list_fenlei=[]
line_fenlei=file2.readline()
list_spmc=[]
line_spmc=file3.readline()
xtgs=[]
while line_mc:
    line_mc=file1.readline()
    list_mc.append(line_mc)
while line_fenlei:
    line_fenlei=file2.readline()
    list_fenlei.append(line_fenlei)
while line_spmc:
    line_spmc=file3.readline()
    list_spmc.append(line_spmc)
for count_1 in range(0,len(list_spmc)):
    a=list_spmc[count_1].decode('utf-8')
    for count_3 in range(0,len(list_mc)):
        num=0
        b=list_mc[count_3].decode('utf-8')
        for count_2 in range(0,len(a)):
            for count_4 in range(0,len(b)):
                if a[count_2]==b[count_4]:
                    num=num+1
        xtgs.append(num)
        #c=xtgs.reverse()
    d=np.array(xtgs)
    sortedDistIndicies=np.argsort(-d)
    classCount={}
    for i in range(0,100):
        voteIlabel=list_fenlei[sortedDistIndicies[i]]
        classCount[voteIlabel]=classCount.get(voteIlabel,0)+1
    sortedClassCount=sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
    file4.write(sortedClassCount[0][0])
    for i in range(0,len(xtgs)):
        del xtgs[0]
    classCount.clear()
    print 'o'
file1.close()
file2.close()
file3.close()
file4.close()


