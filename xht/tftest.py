import tensorflow as tf 
import numpy as np 
a = [1,2,3]
b= tf.reduce_mean(a) 
with tf.Session() as sess:
    sess.run(b)
    print(sess.run(b))