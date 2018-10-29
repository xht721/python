import tensorflow as tf 
from  tensorflow.examples.tutorials.mnist import input_data 
mnist = input_data.read_data_sets('MNIST_data',one_hot=True)

# def layer
def add_layer(inputs, in_size , out_size , activation_function=None):
    with tf.name_scope("Weights"):
        Weights = tf.Variable(tf.random_normal([in_size,out_size]))
    with tf.name_scope("biases"):
        biases = tf.Variable(tf.zeros([1,out_size])+0.1)
    with tf.name_scope("Wx_plus_b"):
        Wx_plus_b = tf.matmul(inputs,Weights) + biases
    if activation_function is None:
        return Wx_plus_b
    else:
        return activation_function(Wx_plus_b)
with tf.name_scope("inputs"):
    xs = tf.placeholder(tf.float32,[None,784])
    ys = tf.placeholder(tf.float32,[None,10])

def compute_accuracy(v_xs,v_ys):
    global prediction
    y_pre = sess.run(prediction,feed_dict={xs:v_xs})
    correct_prediction = tf.equal(tf.argmax(y_pre,1),tf.argmax(v_ys,1))
    
    accuracy = tf.reduce_mean(tf.cast(correct_prediction,tf.float32))
    result = sess.run(accuracy,feed_dict={xs:v_xs,ys:v_ys})
    return result


prediction = add_layer(xs,784,10,activation_function=tf.nn.softmax)

cross_entropy = tf.reduce_mean(-tf.reduce_sum(ys*tf.log(prediction),reduction_indices=[1]))
train = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)
init =  tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    for i in range(100):
        batch_xs,batch_ys = mnist.train.next_batch(100)
        sess.run(train,feed_dict={xs:batch_xs,ys:batch_ys})
        if i % 20 == 0:
            print(compute_accuracy(mnist.test.images,mnist.test.labels))
# print(mnist.test)

