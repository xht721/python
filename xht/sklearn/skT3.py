from  sklearn  import preprocessing
import sklearn as skl
import numpy as np 
import  matplotlib.pyplot as plt 
from sklearn.datasets.samples_generator import make_classification
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.cross_validation import cross_val_score 
from sklearn.neighbors import KNeighborsClassifier

iris = skl.datasets.load_iris()
x = iris.data
y = iris.target
for i in range(1,50):
    knn =  KNeighborsClassifier(n_neighbors=i)
    # knn.fit(x,y)
    # score = knn.score(x,y)
    scores = cross_val_score(knn,x,y,cv=5,scoring='accuracy')
    print("i=%s score=%f" % (i,score ))
    