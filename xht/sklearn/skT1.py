from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.model_selection import train_test_split
from sklearn.datasets.samples_generator import make_classification
from sklearn.svm import SVC
from  sklearn import preprocessing 
import numpy as np

import matplotlib.pyplot as plt 
# iris = datasets.load_iris()
# x = iris.data
# y = iris.target
# # print(x[:2,:],y[:2])
# # print(x.shape)
# x_train , x_test,y_train,y_test =  train_test_split(x , y ,test_size=0.3)
# # print(x_train.shape)
# knn = KNeighborsClassifier()
# knn.fit(x_train,y_train)
# print(knn.predict(x_test))
# print(y_test)

# a = np.array([[10,2.7,3.6],[-100,5,-2],[120,20,40]],dtype=np.float64)
# print(a)
# print(preprocessing.scale(a))
# x,y = datasets.make_regression()
x,y = make_classification(n_samples=300,n_features=2,n_redundant=0,n_informative=2,random_state=22,n_clusters_per_class=1,scale=100)
# x,y =make_classification(n_samples=300,n_redundant=0,n_informative=5,n_classes=3,n_clusters_per_class=2)
# print(x[:1,:])
# print(y)
# plt.scatter(x[:,0],x[:,1],c=y)
# plt.show()
x = preprocessing.scale(x)
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3)
svm = SVC()
svm.fit(x_train,y_train)
print(svm.score(x_test,y_test))