import tensorflow as tf
import numpy as np 
# x_data = np.random.rand(100)
# print(x_data)
# y_data =  x_data*1.2 + 2

weight =  tf.Variable(tf.random_uniform([1],-1.0,1.0))
# biases = tf.Variable(tf.zeros([1]))

# y=weight*x_data + biases

# loss= tf.reduce_mean(tf.square(y-y_data))
# optimizer =  tf.train.GradientDescentOptimizer(0.5)
# train = optimizer.minimize(loss)
# init = tf.initialize_all_variables()
init = tf.global_variables_initializer()

# sess = tf.Session()
# sess.run(init)
# print(sess.run(weight))
# for step in range(100):
#     sess.run(train)
#     print(step,sess.run(weight),sess.run(biases))
print(np.random.uniform([1],-1.0,1.0))
# with tf.Session() as sess:
#     t=  tf.random.uniform([1],-1.0,1.0)
#     sess.run(t)
#     print(t)