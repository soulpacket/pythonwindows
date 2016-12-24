#coding=utf-8
import matplotlib.pyplot as plt
import matplotlib.pyplot as mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']
plt.xlabel(u'性别')
plt.ylabel(u'人数')

plt.xticks((0,1),(u'男',u'女'))

plt.bar(left = (0,1),height = (1,0.5),width = 0.35,align="center")

plt.show()