#preplexity:64
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
dict_1={}  #词:出现次数
list_word=[]
count=0
for i in list_traning:
    #line=file1.readline()
    #count += 1
    a=deque(i.split('  '))
    a.popleft()
    word_num = word_num+len(a)
    for i_1 in a:
        list_word.append(i_1)
        if i_1 not in dict_1:
            dict_1[i_1] = 0
        dict_1[i_1] += 1
dict_2={}  #2-gram 词+词:次数
for i_1 in list_traning:
    b=deque(i_1.split('  '))
    b.popleft()
    if(len(b)>=2):
        for i in range(len(b)-1):
            if b[i]+b[i+1] not in dict_2:
                dict_2[b[i]+b[i+1]]=0
            dict_2[b[i] + b[i + 1]] += 1
p = math.log2(1)
for i in list_test:
    c = deque(i.split('  '))
    c.popleft()
    if(len(c)>=2):
        for i_1 in range(len(c)-1):
            if c[i_1]+c[i_1+1] in dict_2:
                p = p + math.log2(dict_2[c[i_1]+c[i_1+1]]/dict_1[c[i_1]])
                count = count+1
d=-1/count*p
pre=2**d#perplexity
print(pre)
file1.close()