import tensorflow as tf 
import numpy as np 
from tensorflow.examples.tutorials.mnist import input_data
from PIL import Image
def add_layer(input , in_size ,out_size , activation_function = None):
    pass

def compute_accuracy(v_xs,v_ys):
    global prediction
    y_pre = sess.run(prediction, feed_dict={xs: v_xs, keep_prob: 1})
    correct_prediction = tf.equal(tf.argmax(y_pre,1), tf.argmax(v_ys,1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    result = sess.run(accuracy, feed_dict={xs: v_xs, ys: v_ys, keep_prob: 1})
    return result

def weight_variable(shape):
    initial = tf.truncated_normal(shape,stddev=0.1)
    return tf.Variable(initial)

def  biases_variable(shape):
    initial =  tf.constant(0.1,shape=shape)
    return tf.Variable(initial)

def conv2d(x,W):
    return tf.nn.conv2d(x,W,strides=[1,1,1,1],padding='SAME')

def pooling(x):
    return tf.nn.max_pool(x,ksize=[1,2,2,1],strides=[1,2,2,1],padding='SAME')

#read data 
mnist = input_data.read_data_sets('MNIST',one_hot=True)

xs = tf.placeholder(tf.float32,[None,784])
ys = tf.placeholder(tf.float32,[None,10])
keep_prob = tf.placeholder(tf.float32)
x_image = tf.reshape(xs,[-1,28,28,1])

##conv1 layer
W_conv1 = weight_variable([5,5,1,32])
b_conv1 = biases_variable([32])
h_conv1 = tf.nn.relu( conv2d(x_image,W_conv1) + b_conv1)
h_pool1 = pooling(h_conv1)

##conv2 layer
W_conv2 = weight_variable([5,5,32,64])
b_conv2 = biases_variable([64])
h_conv2 = tf.nn.relu( conv2d(h_pool1,W_conv2) + b_conv2)
h_pool2 = pooling(h_conv2)

## func1 layer 
w_fc1 =  weight_variable([7*7*64,1024])
b_fc1 = biases_variable([1024])
h_pool2_flat = tf.reshape(h_pool2,[-1,7*7*64])
h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat,w_fc1)+ b_fc1)
h_fc1_dropout = tf.nn.dropout(h_fc1,keep_prob)

## func2 layer 

w_fc2=  weight_variable([1024,10])
b_fc2 = biases_variable([10])

prediction = tf.nn.softmax(tf.matmul(h_fc1_dropout,w_fc2)+ b_fc2)
# h_fc1_dropout = tf.nn.dropout(h_fc1,keep_prob)


cross_entropy = tf.reduce_mean( -tf.reduce_sum (ys* tf.log(prediction),reduction_indices=[1]))

train =  tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)

init  =  tf.global_variables_initializer()
def loadimage(filename):
    img  =  Image.open(filename).convert('L')
    iarray = np.asarray(img , dtype="float32")
    iarray =np.reshape(iarray,[-1,784])
    # print(img)
    # print(array)
    return iarray


with tf.Session() as sess:
    sess.run(init)
    for i in range(10000):
        batch_xs , batch_ys = mnist.train.next_batch(100)
        sess.run(train,feed_dict={xs:batch_xs,ys:batch_ys,keep_prob:0.5})
        if i % 50 == 0:
            print(compute_accuracy(
            mnist.test.images[:1000], mnist.test.labels[:1000]))
    saver = tf.train.Saver()
    saver.save(sess,'d:\\my_net\\cnn1.ckpt')

    # imgArray = loadimage('D:\\test_0.jpg')
    # # i_arr = tf.cast(imgArray,tf.float32)
    # # i_arr = tf.reshape(i_arr , [-1,784]) 
    # max_index = sess.run(prediction,feed_dict={xs:imgArray,keep_prob:1})
    # index = np.argmax(max_index)
    # print(index)





