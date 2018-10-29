import numpy as np 
import matplotlib.pyplot as plt 
# a = [[1,2,3],
#     [4,5,6]]
# # print(np.array(a).ndim)
# # # print(np.array(a).ndim)
# b = np.arange(12)
# # c= np.stack(b,axis=0)

# # print(b)
# print(b.ndim)
# print(c.ndim)
# print(c)
# a = [1, 2, 3, 4]
# b = [5, 6, 7, 8]
# d = np.stack((a, b),axis=0)
# print(d)
# print(d.ndim)
# a = [1, 2, 3, 4]
# b = [5, 6, 7, 8]
# d = np.stack((a,b),axis=1)
# # print(d)
# test_1 = np.array([[1, 2, 3], [4, 5, 6]])
# test_2 = np.array([[11, 12, 13], [14, 15, 16]])
# # # 0,1,2分别代表所有，行合并，列合并
# # print(np.stack((test_1, test_2), axis=2))
# # print(np.stack((test_1, test_2), axis=1))
# # print(np.stack((test_1, test_2), axis=0))
# print(test_1.ndim)
# print(np.stack(test_1,axis=0))

# a = np.array([[3,4],
#               [4,6]])
# b = np.array([[3,6],[4,1]])
# print(a,"\n",b)
# c=np.dot(a,b)
# # print(c)
# while True:
#     rand = np.random.random()
#     print(rand)
# #     if rand>0.8 :
# #         break

# rand = np.random.random([2,4])
# print(rand)
# sum = np.sum(rand,axis=2)
# print(sum)
# A = np.mat("0,1,2;1,0,3;4 -3 8")
# print(A)
# inv = np.linalg.inv(A)
# print(inv)
# # print(np.dot(A,inv))

# a = np.array([[1,1],[4,2]])
# print(a)
# c = np.array([15,50])
# print(c)
# x = np.linalg.solve(a,c)
# print(x)

t = [1960. , 1961. , 1962. ,1963.,1964.,1965.,1966.,1967.,1968.]
s = [29.72 ,30.61 ,31.51 ,32.13 , 32.34 ,32.85 , 33.56 ,34.20 ,34.83]
xdata =  np.vstack([t,np.ones(len(t))]).T
ydata =  np.log(np.array(s))
a , b = np.linalg.lstsq(xdata ,ydata  )[0]
print(a,b)

pro =  a * 2000 + b
print(pro)

# plt.plot(t , s , 'r^')
# plt.plot(t , int(a*t+b)  )
# plt.show()