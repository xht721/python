import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.cluster import KMeans
x = []
y = [[32.1,120]]
with  open('d:/city.txt','r')  as f:
    for v in f :
        x.append([float(v.split('\t')[2]), float(v.split('\t')[3] )] )
        # print(x)

x = np.array(x)
# print(x)
# print(x[True ,0])
n_cluster = 5
cls = KMeans(n_cluster).fit(x)

# print(cls.labels_)
# print(cls.predict(y))
markers = ['^','x','o','*','+' ]
for i in range(n_cluster):
    # print(i)
    members = cls.labels_==i

    print(type(members))
    print(members)
    # print(x[members,0],x[members,1])
    # plt.scatter(x[members,0],x[members,1],s=60,marker=markers[i],c='b', alpha=0.5)

# plt.show()