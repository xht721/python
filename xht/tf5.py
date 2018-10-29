import tensorflow as tf 
import numpy as np 
import  matplotlib.pyplot as plt
def add_layer(input , input_size ,output_size ,activation_function = None):
    with tf.name_scope('layer'):
        with tf.name_scope('weight'):
            weight = tf.Variable(tf.random_normal([input_size,output_size]),name='w')
        with tf.name_scope('basies'):
            basies = tf.Variable(tf.zeros([1,output_size]),name='b')
        with tf.name_scope('wx_plus_b'):
            wx_plus_b =  tf.matmul(input,weight)+basies
        # output = None
        if activation_function is None:
            output = wx_plus_b
        else:
            output = activation_function(wx_plus_b)
        return output



x_data =  np.linspace(-1 ,1 ,300)
# print(x_data)
# x_dataN =  np.stack(x_data,axis=0).T
# print(x_dataN)
x_dataN1 = x_data[:,np.newaxis]
# print(x_dataN1.shape)
noise =  np.random.normal(0,0.05,x_dataN1.shape)
y= x_dataN1**3 + 0.3 + noise
with tf.name_scope('input'):
    xs = tf.placeholder(tf.float32, [None,1],name='x_input')
    ys = tf.placeholder(tf.float32,[None,1],name='y_input')


l1 = add_layer(xs,1,3,activation_function=tf.nn.relu)
# l1 = add_layer(xs,1,2,activation_function=None)
prediction = add_layer(l1,3,1,activation_function=None)
with tf.name_scope('loss'):
    loss = tf.reduce_mean( tf.reduce_sum( tf.square(prediction-ys) , reduction_indices= 1))
with tf.name_scope('train'):
    train = tf.train.GradientDescentOptimizer(0.1).minimize(loss)
init  =  tf.global_variables_initializer()


plt.scatter(x_dataN1 , y)
plt.ion()
with tf.Session() as sess:
    # tf.summary.FileWriter('d:/logs',sess.graph)
    sess.run(init)
    for i in range(200):
        sess.run(train,feed_dict={xs:x_dataN1,ys:y})
        print(sess.run(loss,feed_dict={xs:x_dataN1,ys:y}))
        prediction_value = sess.run(prediction,feed_dict={xs:x_dataN1})
        lines =plt.plot(x_dataN1,prediction_value,c='r')
        plt.pause(0.01)
        plt.Line2D.remove(lines[0])



plt.show()