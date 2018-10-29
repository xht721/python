from snownlp import SnowNLP
# str = u'你们态度太差了'
# str = u'我没有任何问题了'
# str = u'谢谢你的帮助'
# str = u'你们这个都不能帮我实现嘛'
# str = u'我昨天取的钱怎么还没到账'
# str = u'好的，非常感谢'
str = u'我要投诉你'
s = SnowNLP(str)
print(s.sentiments )
# fun1= lambda x,y: x+y
# print(fun1(1,2))