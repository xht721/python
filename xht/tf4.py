import tensorflow as tf 
import numpy as np 
import pickle 

x_data = np.random.rand(100)
y_data = x_data*0.2 + 0.5
# print(x_data)


weights  = tf.Variable(tf.random_uniform([1],-1.0 , 1.0))
biases =  tf.Variable(tf.zeros([1]))

y =  weights * x_data + biases

loss =  tf.reduce_mean(tf.square(y-y_data))
optimizer =  tf.train.GradientDescentOptimizer(0.5)
train  = optimizer.minimize(loss)

init = tf.global_variables_initializer()

# sess = tf.Session()
# sess.run(init)

# with tf.Session() as sess:
#     sess.run(init)
#     for step in range(100):
#         sess.run(train)
#         print(sess.run(weights),sess.run(biases))

print(tf.random_normal([2,3])[:1,:])


# with open("d:\tf.pickle",'r') as f:
#     pickle.dump()