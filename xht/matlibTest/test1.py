import matplotlib.pyplot as plt 
import numpy as np 
x = np.linspace(-1,1,50)
y = x**2 +1 
# print(a)
plt.figure()
plt.plot(x,y,color="red",linewidth=1,linestyle="--")
plt.xlabel("x label")
plt.ylabel("y label")
plt.xlim((0,1))
plt.xlim((0,10))
plt.xticks([-1,0,1],[r"bad",r"$normal$",r"好"],fontproperties="FangSong")

ax = plt.gca()
ax.spines['top'].set_color("none")
ax.xaxis.set_ticks_position("bottom")
ax.spines["bottom"].set_position(("data",1.4))
# ax.xaxis.set_ticks_position("buttom")
# ax.xaxis.set_ticks_position("bottom")
plt.show()