import tensorflow as tf 
import numpy as np
import matplotlib.pyplot as plt  

def layer(input , input_size , output_size , activation_function=None):
    with tf.name_scope('layer'):
        with tf.name_scope('weights'):
            weights = tf.Variable( tf.random_normal([input_size,output_size]),name="wei")
        with tf.name_scope('biases'):
            biases = tf.Variable(tf.zeros([1,output_size]))
        with tf.name_scope('wx_plus_b'):
            wx_plus_b = tf.matmul(input,weights) + biases
        if activation_function is None:
            output = wx_plus_b
        else:
            output = activation_function(wx_plus_b)
            
        return output

x_data = np.linspace(-1,1,300)[:,np.newaxis]
y_data = x_data * 5 - 0.5

with tf.name_scope('inputs'):
    xs = tf.placeholder(tf.float32,[None,1],name="x_input")
    ys = tf.placeholder(tf.float32,[None,1],name="y_input")



l1 = layer(xs,1,10,activation_function=tf.nn.relu)
l2 = layer(l1,10,1,activation_function=None)
with tf.name_scope('loss'):
    loss  = tf.reduce_mean(tf.reduce_sum(tf.square(l2 - ys),reduction_indices=[1]))
with tf.name_scope('optimizer'):
    optimizer = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

init = tf.global_variables_initializer()



# fig =  plt.figure()
# ax = fig.add_subplot(1,1,1)
# ax.scatter(x_data,y_data)
# plt.show()


with tf.Session() as sess:
    sess.run(init)
    write = tf.summary.FileWriter("d:/logs",sess.graph)
#     for n in range (1000):
#         sess.run(optimizer,feed_dict={xs:x_data,ys:y_data})
#         if n%10  :
#             # print(n,sess.run(weights) ,sess.run(biases))
#             print(sess.run(loss,feed_dict={xs:x_data,ys:y_data}))
