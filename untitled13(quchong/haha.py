#coding:utf-8
file1=open("moban.txt","r")
file2=open("mobanmc.txt","r")
file3=open("yaoqiu.txt","r")
file4=open("yaomc.txt","wb")
moban=[]
mobanmc=[]
line1=file1.readline()
line2=file2.readline()
line3=file3.readline()
while line1 :
    line1=file1.readline()
    moban.append(line1)
while line2 :
    line2=file2.readline()
    mobanmc.append(line2)
while line3 :
    line3=file3.readline()
    for i in range(0,len(moban)):
        if line3==moban[i]:
            file4.write(mobanmc[i])
            #file4.write("\n")
            break
    if line3!=moban[i]:
        file4.write("\n")
file1.close()
file2.close()
file3.close()
file4.close()
