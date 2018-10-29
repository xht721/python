import pandas as pd 
import numpy as np 
# A = pd.Series([1,2,3,54,2,'gf','ds'])
# print(A)
# dates = pd.date_range('20180408',periods=6)
# df = pd.DataFrame(np.random.randn(24).reshape(6,4),index=dates ,columns=['A','B','C','D'] )
# print(df['A'])
# print(np.linspace(-1,1,300))
# x = np.linspace(-1,1,300)[:,np.newaxis]
# print(x.shape)
num = np.ones(10).reshape(2,5)
print(num.shape)
a = np.array([2,3]).T
print(a.shape)
mul = np.matmul(a,num)
print(mul)