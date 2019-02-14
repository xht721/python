import numpy as np 
import tensorflow as tf 
import matplotlib.pyplot as plt 

x_date = [338.,333.,328.,207.,226.,25.,179.,60.,208.,606.]
# x_datex = x_date[:,np.newaxis ]
y_date = [640.,633.,619.,393.,428.,27.,193.,66.,226.,1591.]
plt.figure()
plt.scatter(x_date,y_date)



#method1 use machelearning
# y_date = b + w*x_date
# b = -62
# w = -100
# lr = 0.000001
# iteration = 1500000
# b_history = [b]
# w_history = [w]

# for i in range(iteration):
#   # 求Σ值 start
#     b_grad = 0.0
#     w_grad = 0.0
#     for n in range(len(x_date)):
#             w_grad = w_grad -2.0*x_date[n]*(y_date[n] - (w*x_date[n]+b))
#             b_grad = b_grad -2.0*(y_date[n] - (w*x_date[n]+b))
    
#     w = w - lr*w_grad
#     b = b - lr*b_grad
#     loss = 0.0
#     for n in range(len(x_date)):
#         loss += (y_date[n] - (w*x_date[n] +b ))

#     if iteration % 5000 == 0 :
#         print("loss value is %f %f %f " % (loss,w,b))

# method2 use TensorFlow 
w = tf.Variable(np.random.randn(1))
b = tf.Variable(np.random.randn(1))
y = w*x_date + b
loss = tf.reduce_mean(tf.square(y_date-y))
optimizer = tf.train.GradientDescentOptimizer(0.00001)
train =  optimizer.minimize(loss)
init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    for i in range(900001):
        sess.run(train)
        if i%200 == 0 :
          # print(sess.run("w value: %d , b value： %d " %w,b))
          print("w value: %f , b value： %f " % (sess.run(w),sess.run(b)))
          # plt.plot()
          # plt.show()


