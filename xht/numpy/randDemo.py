import numpy as np 
import tensorflow as tf 
# rand 参数跟的是产生随机数的形状 0~1分布的随机数
# v1 = np.random.rand()
# print(v1)
# v2 = np.random.rand(2,2,3)
# print(v2)
# print(v2.ndim)

# randn 参数跟的是产生随机数的形状 标准正态分布的随机数
# v3 = np.random.randn()
# print(v3)
# v4 = np.random.rand(2,2,3)
# print(v4)
# print(v4.ndim)

# randint 返回随机整数，参数low~high 不包含high size 如果需要制定形状，需要传入一个tulpu 例如（2,2）
# v5 = np.random.randint(10,20,(2,2))
# print(v5)

#random_normal  返回的正态分数随机数，可指定期望u 和方差
v6 = tf.random_normal((2,2),1,2)
with tf.Session() as sess:
    print(sess.run(v6))
