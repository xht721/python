#from functools import reduce  # py3
import pickle
# a = int(input("please input:"))
# if a>60:
#     print("ok")
# else:
#     print("bad")
# 

# sum = reduce(lambda x,y:x+y ,range(1,101))
# print(sum)
# fo  = open(r"D:\Project\pyProject\test.txt","a+")
# print(fo.read())
# fo.write("aaaaaa")
# print(fo.read())
# fo.close()


lista = ["a","b","c"]
f1 = open("d:\\1.pk1","wb")
pickle.dump(lista,f1,True)
f1.close()

f2 = open("d:\\1.pk1","rb")
print(f2.read())
t = pickle.load(f2)
print(t)
f2.close()
