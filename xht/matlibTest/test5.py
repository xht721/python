import matplotlib.pyplot as plt
import numpy as np 
x = np.linspace(-100,100,100)
print(x)
y = x**2 + 2 
plt.figure()
plt.plot(x,y)
# plt.show()