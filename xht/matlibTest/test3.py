import matplotlib.pyplot as plt 
import numpy as np  

# x = [1,2,3,4]
# y = [3,5,10,25]

# f1 = plt.figure()
# ax1 = f1.add_subplot(231)
# plt.plot(x,y,marker="D")
# plt.sca(ax1)
x= [np.arange(1,2,0.1),np.arange(3,4,0.1),np.arange(99,100,0.1)]
plt.imshow(x)
plt.colorbar()
plt.show()