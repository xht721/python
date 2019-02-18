import tensorflow as tf 
from tensorflow.examples.tutorials.mnist import  input_data

mnist = input_data.read_data_sets("D:\project\python\MNIST_data",one_hot=True)

batch_size = 100
n_batch = mnist.train.num_examples // batch_size
print(n_batch)