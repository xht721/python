import tensorflow as tf 
import numpy as  np 
from PIL import Image 
from tensorflow.examples.tutorials.mnist import input_data

# mnist =  input_data.read_data_sets('MNIST',one_hot=True)
# batch_xs , batch_ys  =  mnist.train.next_batch(1)
# print(batch_xs.shape)


def loadimage(filename):
    img  =  Image.open(filename).convert('L')
    array =  np.asarray(img,dtype='float32')
    return np.reshape(array,[-1,28,28,1])
    # array = np.asarray(img , dtype="float32")
    # array = tf.reshape(array , [1,784]) 
    # print(img)
    # print(array.shape)
    # return array


def conv(x,W):
    return tf.nn.conv2d(x,W,strides=[1,1,1,1],padding='SAME')

def pooling(x):
    return tf.nn.max_pool(x,ksize=[1,2,2,1],strides=[1,2,2,1],padding='SAME')

def weight_variable(shape):
    return tf.Variable(tf.truncated_normal( shape,stddev=0.1 ))

def biases_varialbe(shape):
    return tf.Variable(tf.constant(0.1,shape=shape))

# xs  = tf.placeholder(tf.float32,[28,28])
ys =  tf.placeholder(tf.float32,[None,10])
x_image =  tf.placeholder(tf.float32,[None,28,28,1]) 

#conv1
conv1 = tf.nn.relu(conv(x_image,weight_variable([5,5,1,32]))+biases_varialbe([32]))
pool1 = pooling(conv1)

#conv2
conv2 = tf.nn.relu(conv(pool1,weight_variable([5,5,32,64]))+biases_varialbe([64]))
pool2 = pooling(conv2)
#full1
fu1_lay =  tf.nn.relu ( tf.matmul(tf.reshape(pool2,[-1,7*7*64]), weight_variable([7*7*64,1024]) ) + biases_varialbe([1024]))

#full2

w_fc2=  weight_variable([1024,10])
b_fc2 = biases_varialbe([10])

prediction = tf.nn.softmax( tf.matmul(fu1_lay,w_fc2)+b_fc2)
saver =  tf.train.Saver()

with tf.Session() as sess:
    saver.restore(sess ,'d:\\my_net\\cnn1.ckpt')
    pre_index =  sess.run(prediction,feed_dict={x_image:loadimage('D:\\test_3.jpg')})
    print(np.argmax(pre_index))
# loadimage('D:\\test_3.jpg')