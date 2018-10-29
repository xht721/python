import tensorflow as tf 
import numpy as np 
import matplotlib.pyplot as plt 
def add_layer(inputs , input_size , output_size , activation_function=None):
    with tf.name_scope("layer"):
        with tf.name_scope("Weight"):
            Weight = tf.Variable(tf.random_normal([input_size,output_size]))
        with tf.name_scope("biases"): 
            biases = tf.Variable(tf.zeros([1,output_size])+0.1)
        with tf.name_scope("Wx_b"):
            Wx_b = tf.matmul(inputs,Weight) +biases
        # print("wx_b===========",Wx_b)
        if activation_function is None:
            outputs = Wx_b
        else:
            outputs = activation_function(Wx_b)
        return outputs

x_data = np.linspace(-1,1,100)[:,np.newaxis]
noise = np.random.normal(0,0.05,x_data.shape)
y_data = np.square(x_data)-0.5 + noise

# print(y_data , y_data.shape)
#print(noise)
with tf.name_scope("input"):
    xs = tf.placeholder(tf.float32,[None,1])
    ys = tf.placeholder(tf.float32,[None,1])

l1 = add_layer(xs,1,10,activation_function=tf.nn.relu)
# print(l1)
prediction = add_layer(l1,10,1,activation_function=None)
with tf.name_scope("loss"):
    loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys-prediction),reduction_indices=[1]))
with tf.name_scope("train"):
    train = tf.train.GradientDescentOptimizer(0.1).minimize(loss)
init = tf.global_variables_initializer()


# fig  = plt.figure() 
# ax = fig.add_subplot(1,1,1)
# plt.show()


# plt.subplot(221)  
# plt.plot(x, x)  

# x = np.arange(0, 100)  
# fig  = plt.figure()
# ax = fig.add_subplot(1,1,1)  
# ax.scatter(x_data,y_data) 
# plt.ion()  
# plt.show(block=False) 




# a = tf.Variable(tf.random_normal([2,2],seed=3))
# # b = tf.Variable(tf.truncated_normal([2,2],seed=2))
# init = tf.global_variables_initializer()


with tf.Session() as sess:
    sess.run(init)
#     for i in range(1000):
#         sess.run(train,feed_dict={xs:x_data,ys:y_data})
#         if i % 20 == 0:
#             # print(sess.run(loss,feed_dict={xs:x_data,ys:y_data}))
#             prediction_value = sess.run(prediction,feed_dict={xs:x_data})
#             lines = ax.plot(x_data,prediction_value,'r-',lw=5)
#             plt.pause(0.1)
#             ax.lines.remove(lines[0])
            

    
    
tf.summary.FileWriter("logs",sess.graph)