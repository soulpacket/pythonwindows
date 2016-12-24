#798/4000 when string>4 864/4000 when string>5  782/4000 wheb string>3
import re
from os import listdir
from numpy import *
count = -1
docList = []
classList = []
num_1 = []
for i in listdir('20_newsgroups'):
    num=0
    count+=1
    if count ==0:
        continue
    else :
        for i_1 in listdir('20_newsgroups/'+i):
            num+=1
            #print(i_1)
            if num==1:
                continue
            else:
                f = open('20_newsgroups/'+i+'/'+i_1,'rb')
                a = f.read()  # 得到所有byte字符
                b = re.search(b'\n\n(.*)', a, re.S).group()  # 得到第一个两个换行符之后的所有字符
                text = b.lower()  # 全部转化为小写
                # print(text)
                regx = re.split(b'\W*', text)  # 筛选出所有的字母和数字(去掉各种符号),但是包含了空字符
                list_1 = []  # 将byte字符转化为str字符
                for i_2 in regx:
                    c = re.findall('\'(.*?)\'', str(i_2))[0]
                    if len(c) > 3:  # 筛选出字符数大于2的字符串
                        list_1.append(c)
                #print(list)#字符全部进入到list
                docList.append(list_1)
                classList.append(count)
    num_1.append(num-1)
    # if count==2:
    #     break
print(type(docList))
print(len(classList))#[1..20]
def createVocabList(dataSet):
    vocabSet = set()  #create empty set
    for document in dataSet:
        vocabSet = vocabSet | set(document) #union of the two sets
    print('creatfinish')
    return list(vocabSet)
def setOfWords2Vec(vocabList, inputSet):
    returnVec = [0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
        #else: print "the word: %s is not in my Vocabulary!" % word
    return returnVec
def trainNB0(trainMatrix,trainCategory):
    numTrainDocs = len(trainMatrix)
    numWords = len(trainMatrix[0])
    #pAbusive = sum(trainCategory)/float(numTrainDocs)
    p2Num = ones(numWords); p1Num = ones(numWords)      #change to ones()
    p3Num = ones(numWords)
    p4Num = ones(numWords);p8Num = ones(numWords);p12Num = ones(numWords);p15Num = ones(numWords);p18Num = ones(numWords)
    p5Num = ones(numWords);p9Num = ones(numWords);p13Num = ones(numWords);p16Num = ones(numWords);p19Num = ones(numWords)
    p6Num = ones(numWords);p10Num = ones(numWords);p14Num = ones(numWords);p17Num = ones(numWords);p20Num = ones(numWords)
    p7Num = ones(numWords);p11Num = ones(numWords)
    p2Denom = 2.0; p1Denom = 2.0                        #change to 2.0
    p3Denom = 2.0;p6Denom = 2.0;p9Denom = 2.0;p11Denom = 2.0;p13Denom = 2.0;p15Denom = 2.0;p17Denom = 2.0;p19Denom = 2.0
    p4Denom = 2.0;p7Denom = 2.0;p10Denom = 2.0;p12Denom = 2.0;p14Denom = 2.0;p16Denom = 2.0;p18Denom = 2.0;p20Denom = 2.0
    p5Denom = 2.0;p8Denom = 2.0
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:
            p1Num += trainMatrix[i]
            p1Denom += sum(trainMatrix[i])
        elif trainCategory[i]==2:
            p2Num += trainMatrix[i]
            p2Denom += sum(trainMatrix[i])
        elif trainCategory[i] == 3:
            p3Num += trainMatrix[i]
            p3Denom += sum(trainMatrix[i])
        elif trainCategory[i] == 4:
            p4Num += trainMatrix[i]
            p4Denom += sum(trainMatrix[i])
        elif trainCategory[i] == 5:
            p5Num += trainMatrix[i]
            p5Denom += sum(trainMatrix[i])
        elif trainCategory[i] == 6:
            p6Num += trainMatrix[i]
            p6Denom += sum(trainMatrix[i])
        elif trainCategory[i] == 7:
            p7Num += trainMatrix[i]
            p7Denom += sum(trainMatrix[i])
        elif trainCategory[i] == 8:
            p8Num += trainMatrix[i]
            p8Denom += sum(trainMatrix[i])
        elif trainCategory[i] == 9:
            p9Num += trainMatrix[i]
            p9Denom += sum(trainMatrix[i])
        elif trainCategory[i] == 10:
            p10Num += trainMatrix[i]
            p10Denom += sum(trainMatrix[i])
        elif trainCategory[i] == 11:
            p11Num += trainMatrix[i]
            p11Denom += sum(trainMatrix[i])
        elif trainCategory[i] == 12:
            p12Num += trainMatrix[i]
            p12Denom += sum(trainMatrix[i])
        elif trainCategory[i] == 13:
            p13Num += trainMatrix[i]
            p13Denom += sum(trainMatrix[i])
        elif trainCategory[i] == 14:
            p14Num += trainMatrix[i]
            p14Denom += sum(trainMatrix[i])
        elif trainCategory[i] == 15:
            p15Num += trainMatrix[i]
            p15Denom += sum(trainMatrix[i])
        elif trainCategory[i] == 16:
            p16Num += trainMatrix[i]
            p16Denom += sum(trainMatrix[i])
        elif trainCategory[i] == 17:
            p17Num += trainMatrix[i]
            p17Denom += sum(trainMatrix[i])
        elif trainCategory[i] == 18:
            p18Num += trainMatrix[i]
            p18Denom += sum(trainMatrix[i])
        elif trainCategory[i] == 19:
            p19Num += trainMatrix[i]
            p19Denom += sum(trainMatrix[i])
        elif trainCategory[i] == 20:
            p20Num += trainMatrix[i]
            p20Denom += sum(trainMatrix[i])
    p1Vect = log(p1Num/p1Denom)          #change to log()
    p2Vect = log(p2Num/p2Denom)          #change to log()
    p3Vect = log(p3Num / p3Denom)
    p4Vect = log(p4Num / p4Denom)
    p5Vect = log(p5Num / p5Denom)
    p6Vect = log(p6Num / p6Denom)
    p7Vect = log(p7Num / p7Denom)
    p8Vect = log(p8Num / p8Denom)
    p9Vect = log(p9Num / p9Denom)
    p10Vect = log(p10Num / p10Denom)
    p11Vect = log(p11Num / p11Denom)
    p12Vect = log(p12Num / p12Denom)
    p13Vect = log(p13Num / p13Denom)
    p14Vect = log(p14Num / p14Denom)
    p15Vect = log(p15Num / p15Denom)
    p16Vect = log(p16Num / p16Denom)
    p17Vect = log(p17Num / p17Denom)
    p18Vect = log(p18Num / p18Denom)
    p19Vect = log(p19Num / p19Denom)
    p20Vect = log(p20Num / p20Denom)
    return p1Vect,p2Vect,p3Vect,p4Vect,p5Vect,p6Vect,p7Vect,p8Vect,p9Vect,p10Vect,p11Vect,p12Vect,p13Vect,p14Vect,p15Vect,p16Vect,p17Vect,p18Vect,p19Vect,p20Vect
#createVocabList(docList)
def classifyNB(vec2Classify, p1Vect, p2Vect,p3Vect,p4Vect,p5Vect,p6Vect,p7Vect,p8Vect,p9Vect,p10Vect,p11Vect,p12Vect,p13Vect,p14Vect,p15Vect,p16Vect,p17Vect,p18Vect,p19Vect,p20Vect):
    list_1 = []
    list_1.append(sum(vec2Classify * p1Vect))    #element-wise mult
    list_1.append(sum(vec2Classify * p2Vect))
    list_1.append(sum(vec2Classify * p3Vect))
    list_1.append(sum(vec2Classify * p4Vect))
    list_1.append(sum(vec2Classify * p5Vect))
    list_1.append(sum(vec2Classify * p6Vect))
    list_1.append(sum(vec2Classify * p7Vect))
    list_1.append(sum(vec2Classify * p8Vect))
    list_1.append(sum(vec2Classify * p9Vect))
    list_1.append(sum(vec2Classify * p10Vect))
    list_1.append(sum(vec2Classify * p11Vect))
    list_1.append(sum(vec2Classify * p12Vect))
    list_1.append(sum(vec2Classify * p13Vect))
    list_1.append(sum(vec2Classify * p14Vect))
    list_1.append(sum(vec2Classify * p15Vect))
    list_1.append(sum(vec2Classify * p16Vect))
    list_1.append(sum(vec2Classify * p17Vect))
    list_1.append(sum(vec2Classify * p18Vect))
    list_1.append(sum(vec2Classify * p19Vect))
    list_1.append(sum(vec2Classify * p20Vect))
    return list_1.index(max(list_1))
    # if p1 > p0:
    #     return 1
    # else:
    #     return 0
vocaList = createVocabList(docList)
trainingSet = list(range(19981))
testSet = []
for i in range(4000):
    print(i)
    randIndex = int(random.uniform(0,len(trainingSet)))
    testSet.append(trainingSet[randIndex])
    del (trainingSet[randIndex])
trainMat = []
trainClasses = []
count_1 =0
for i in trainingSet:
    count_1+=1
    print(count_1)
    trainMat.append(setOfWords2Vec(vocaList,docList[i]))
    trainClasses.append(classList[i])
#p(c|w)=p(w0|ci)*p(w1|ci)
p1Vect,p2Vect,p3Vect,p4Vect,p5Vect,p6Vect,p7Vect,p8Vect,p9Vect,p10Vect,p11Vect,p12Vect,p13Vect,p14Vect,p15Vect,p16Vect,p17Vect,p18Vect,p19Vect,p20Vect=trainNB0(array(trainMat),array(trainClasses))
errorCount = 0
numm=0
for i in testSet:
    numm +=1
    print(numm)
    wordVector = setOfWords2Vec(vocaList,docList[i])
    if classifyNB(array(wordVector),p1Vect,p2Vect,p3Vect,p4Vect,p5Vect,p6Vect,p7Vect,p8Vect,p9Vect,p10Vect,p11Vect,p12Vect,p13Vect,p14Vect,p15Vect,p16Vect,p17Vect,p18Vect,p19Vect,p20Vect)+1 !=classList[i]:
        errorCount+=1
print(errorCount)
print(len(testSet))






