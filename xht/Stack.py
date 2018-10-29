class Stack:
    def __init__(self ,size):
        self.size=size
        self.st=[]
        self.top=0
    def isfull(self):
        print(str(self.top)+"===:==="+str(self.size))
        if self.top==self.size:
           
            return True
        else:
            return False
    def isEmple(self):
        if self.top==0:
            return True
        else:
            return False
    def push(self,content):
        if self.isfull():
            print("stack is full")
        else:
            self.st.append(content)
            self.top+=1
    def pull(self):
        if self.isEmple():
            print("stack is emply")
        else:
            self.top-=1
            return self.st.pop()
            
s=Stack(2)
print(s.isEmple())
s.push("aaa")
s.push("aaa")
s.push("aaa")
