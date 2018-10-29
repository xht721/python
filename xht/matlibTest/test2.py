import matplotlib.pyplot as plt 
import numpy as np 
x, y = np.meshgrid(np.arange(-1, 1, 0.01), np.arange(-1, 1, 0.01))
# print(x)
contor = np.sqrt(x ** 2 + y ** 2)
plt.imshow(contor)
# plt.colorbar()
plt.show()