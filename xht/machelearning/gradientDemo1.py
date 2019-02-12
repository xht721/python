import numpy as np 

x_date = [338.,333.,328.,207.,226.,25.,179.,60.,208.,606.]
y_date = [640.,633.,619.,393.,428.,27.,193.,66.,226.,1591.]
# y_date = b + w*x_date
b = -62
w = -100
lr = 0.000001
iteration = 1500000
b_history = [b]
w_history = [w]

for i in range(iteration):
  # 求Σ值 start
    b_grad = 0.0
    w_grad = 0.0
    for n in range(len(x_date)):
            w_grad = w_grad -2.0*x_date[n]*(y_date[n] - (w*x_date[n]+b))
            b_grad = b_grad -2.0*(y_date[n] - (w*x_date[n]+b))
    
    w = w - lr*w_grad
    b = b - lr*b_grad
    loss = 0.0
    for n in range(len(x_date)):
        loss += (y_date[n] - (w*x_date[n] +b ))

    if iteration % 5000 == 0 :
        print("loss value is %f %f %f " % (loss,w,b))

