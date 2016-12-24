# coding:utf-8
import matplotlib as mpl

import matplotlib.pyplot as plt
import numpy as np
custom_font = mpl.font_manager.FontProperties(fname='/Library/Fonts/华文细黑.ttf')
font_size = 10 # 字体大小
fig_size = (10,8.6) # 图表大小

mpl.rcParams['font.sans-serif'] = ['SimHei']
#names = (u'小明', u'小红') # 姓名
shangpin=(u'无',3005623,3005310,u'无',3005049,3005168,u'无',3005331,30054063005433,1012002,3005141)
subjects = (u'搬不动',u'电子',u'二赠一',u'清仓',u'清洁',u'日用',u'扫码购',u'食品',u'特惠',u'饮料',u'赠品')
scores = (0,397,1401,0,730,889,0,1185,108,915,550) # 成绩
mpl.rcParams['font.size'] = font_size
mpl.rcParams['figure.figsize'] = fig_size
bar_width = 0.35
index = np.arange(len(scores))##0072BC,byrgcmk
rects1 = plt.bar(index, scores, bar_width, color=('r','g','b','y','c','m','k','#0072BC','#ED1C24','#FF00FF'),align="center",label=shangpin)
plt.xticks(index,subjects)
plt.ylim(ymax=1500, ymin=0)
plt.title(u'各类商品用户点击率最高的商品sn号及次数')
plt.xlabel(u'商品类别')
plt.ylabel(u'出现次数')
plt.legend(rects1,shangpin)
# 添加数据标签
def add_labels(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2, height, height, ha='center', va='bottom')
        # 柱形图边缘用白色填充，纯粹为了美观
        rect.set_edgecolor('white')
add_labels(rects1)
plt.show()
# add_labels(rects2)

# 图表输出到本地
#plt.savefig('scores_par.png')