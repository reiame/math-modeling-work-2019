import matplotlib.pyplot as plt

x=[37.6,
30.34,
30.08,
14.48,
47.07,
61.1,
44.8,
57.1,
67.6,
52.53,
44
]
y=[47.59,
41.57,
59.01,
38.9,
54.47,
38.1,
47.9,
59,
53.3,
47.76,
30.6
]
ax = plt.gca()


#ax.xaxis.set_ticks_position('top') #将x轴的位置设置在顶部
#ax.invert_xaxis() #x轴反向


ax.yaxis.set_ticks_position('right') #将y轴的位置设置在右边
#ax.invert_yaxis() #y轴反向

for i in range(11):
    plt.scatter(x[i],y[i],color='r')
plt.axis([0,100,100,0])
plt.show()

