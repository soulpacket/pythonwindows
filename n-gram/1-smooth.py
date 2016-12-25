#add-one:2675
from collections import deque
import math
file1=open('1998.txt',encoding='utf-8')
#line='0'
list_1 = file1.readlines()#每行是一个元素的列表集合
#print(list_1)
line_num=len(list_1)#总行数
#print(line_num)
traning_num=int(line_num*0.9)#训练集的行数
#print(traning_num)
list_traning = list_1[0:traning_num]#训练集list
list_test = list_1[traning_num:line_num]#测试集list
word_num = 0  #总词数
dict_1={}
count=0
for i in list_traning:
    #line=file1.readline()
    #count += 1
    a=deque(i.split('  '))
    a.popleft()
    word_num = word_num+len(a)
    for i_1 in a:
        if i_1 not in dict_1:
            dict_1[i_1] = 1
        dict_1[i_1] += 1
#print(word_num)
p=math.log2(1)
for i in list_test:
    b = deque(i.split('  '))
    b.popleft()
    for i_1 in b:
        if i_1 not in dict_1:
            dict_1[i_1]=1
        if i_1 in dict_1:
            c=math.log2(dict_1[i_1]/(word_num+len(dict_1)))
            #print(dict_1[i_1])
            p = p + c
            count = count+1
#print(p)
d=-1/count*p
pre=2**d#perplexity
print(pre)
file1.close()
