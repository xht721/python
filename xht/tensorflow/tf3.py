import tensorflow as tf  
import numpy as np 
# v1 = tf.placeholder(tf.float32)
# v2 = tf.placeholder(tf.float32)
# mul = tf.multiply(v1,v2)
# with tf.Session() as sess:
#     print(sess.run(mul,feed_dict={v1:[2,3],v2:[3,4]}));
corrent = tf.equal([1,1,1,1,1],[1,2,2,2,1])
accuracy = tf.reduce_mean(tf.cast(corrent,tf.float32))
with tf.Session() as sess:
    print(sess.run(corrent))
    print(sess.run(accuracy))
    