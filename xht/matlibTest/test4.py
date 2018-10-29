import matplotlib.pyplot as plt 
import numpy as np  

x = np.linspace(-1,1,100)
y1 = x**2 + 1
y2 = 3*x + 1
plt.figure(num=1,figsize=(7,7))
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))
# ax.xaxis.set_ticks_position('bottom')
xz = 0.5
yz = xz**2+1
plt.scatter(xz,yz)


plt.plot(x,y1,label="blue")
plt.plot([0.5,0.5],[0.5**2+1,0],'--')
plt.plot(x,y2,c='r',label="red")
plt.annotate(r'this is annotata',xy=(xz,yz),xycoords='data',xytext=(0.7,0.7),textcoords="offset points",
arrowprops=dict(arrowstyle="->",connectionstyle="arc3,rad=.5"))
plt.xlim(-1,1)
plt.ylim(-0.5,3)
plt.legend(loc="best")
plt.show()
