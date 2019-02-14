import tensorflow as tf
import numpy as np 
# x_data = np.linspace(-1,1,300)[:,np.newaxis]
# print(x_data)
# print(tf.random_normal([1,4]).shape)
x_data = np.linspace(1,2,20)#[:,np.zeros]
print(x_data[0,1])
# print(x_data)
# x_data = tf.cast(x_data,dtype=tf.float32)
# w =tf.Variable( tf.random_normal([2,5]) )
# wx =  tf.multiply(x_data,w)

# init = tf.global_variables_initializer()
# with tf.Session() as sess:
#     sess.run(init)
#     print(sess.run(w))
#     print(sess.run(wx))