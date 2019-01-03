# -*- coding: utf-8 -*-
import numpy as np
# print ('使用列表生成一维数组')
# data = [1,2,3,4,5,6]
# x = numpy.array(data)
# print( x) #打印数组
# print( x.dtype) #打印数组元素的类型
# print ('使用列表生成二维数组')
# data = [[1,2,9],[3,4,9],[5,6,9]]
# x = numpy.array(data)
# print(data)
# print( x ) #打印数组
# print( x.ndim )#打印数组的维度
# print( x.shape )#打印数组各个维度的长度。shape是一个元组
# print '使用zero/ones/empty创建数组:根据shape来创建'
# x = numpy.zeros(6) #创建一维长度为6的，元素都是0一维数组
# print( x )
# x = numpy.zeros((2,3)) #创建一维长度为2，二维长度为3的二维0数组
# print( x )
# x = numpy.ones((2,3)) #创建一维长度为2，二维长度为3的二维1数组
# print( x)
# x = numpy.empty((3,3)) #创建一维长度为2，二维长度为3,未初始化的二维数组
# print( x )
# x = numpy.zeros([1,2,3])
# print(x)
# print(x.ndim)
# print '使用arrange生成连续元素'
# print numpy.arange(6) # [0,1,2,3,4,5,] 开区间
# print numpy.arange(0,6,2)  # [0, 2，4]
# x = numpy.array([1,2.6,3],dtype = numpy.int64)
# print (x) # 元素类型为int64
# print (x.dtype)
# x = numpy.array([1,2,3],dtype = numpy.float64)
# print (x) # 元素类型为float64
# print (x.dtype)
# x = np.random.rand(100)
# y = np.random.uniform(1,-1,(2,3))
# y1 = np.random.randn(1,1,-1)
# print(y)
# print(x)
# print(y)
# x = np.array([1,2,3,4])
# x1 = x[np.newaxis]
# x2 = x.T[:np.newaxis]
# print(x,x.ndim)
# print(x1,x1.ndim)
# print(x2,x2.shape)
# a=[[[1,2,3],
#    [4,5,6]]]
# print("列表a如下：")
# print(np.array(a).shape)
# a = np.arange(9).reshape(3,3)
# print(a[1])
# for row in a:
#     print(row)
A = np.array([[2,0,0],[2,1,2],[0,3,1]])
Ainv = np.linalg.inv(A)
B = np.array([[1,2,3],[3,2,1],[2,2,3]])
# b1 = np.array([[1,1],[0,1]])
# b2 = np.array([[1,2],[1,1]])
# print(np.dot(b2,b1))
# dev = np.linalg.det(B)
# print(dev)
# 
# print(A1)
E = np.dot(np.dot(Ainv,B),A)
print(E)