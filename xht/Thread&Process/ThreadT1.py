import threading
import time
from queue import Queue

def add_thread():
    print("t1 start")
    # print("add thread %s"% threading.current_thread())
    for i in range(100):
        print("t1 %s" %i)
    # time.sleep(1.5)
    print("t1 end")
def add_thread1():
    print("t2 start")
    for i in range(100):
        print("t2 %s" %i)
    # time.sleep(1)
    print("t2 end")
def main():
    # print(threading.active_count())
    # print(threading.enumerate())
    # print(threading.current_thread())
    t1 = threading.Thread(target=add_thread,name="T1")
    t2 = threading.Thread(target=add_thread1,name="T2")
    t1.start()
    t1.join()
    t2.start()
    
    # print(threading.active_count())
    print("main end")
def complete(li , q ):
    for i in range(len(li)):
        li[i] = li[i]**2
    q.put(li)
def threadCQ():
    input = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
    threads = []
    results = []
    q = Queue()
    for i in range(4):
        t = threading.Thread(target=complete,args=(input[i],q))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    results.append(q.get())
    results.append(q.get())
    results.append(q.get())
    results.append(q.get())
    print(q.empty())

    print(results)
if __name__=='__main__':
    threadCQ()