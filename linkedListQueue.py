import time

class LinkedElement:
    def __init__(self, val):
        self.next = None
        self.value = val
    
class Queue:
    def __init__(self):
        self.last = None
        self.first = None
        self.size = 0
    
    def enqueue(self, value):
        item = LinkedElement(value)
        if(self.first == None):
            self.last = item
            self.first = item
        else:
            self.last.next = item
            self.last = item
    
    def dequeue(self):
        item = self.first.value
        self.first = self.first.next
        return item
    
    
def enqueueDequeue():
    size = 10000000
    q = Queue()

    t1 = time.time()
    
    for i in range(size):
        q.enqueue(i)
    
    for i in range(size):
        q.dequeue()
    
    t2 = time.time()
    print("linkedListQueue.enqueueDequeue(): ", end="")
    print(t2 - t1)
    return

def enqueueTest():
    size = 10000000
    q = Queue()

    t1 = time.time()
    
    for i in range(size):
        q.enqueue(i)
    
    t2 = time.time()
    print("linkedListQueue.enqueueTest(): ", end="")
    print(t2 - t1)
    return


def dequeueTest():
    size = 10000000
    q = Queue()
    for i in range(size):
        q.enqueue(i)
    
    t1 = time.time() 

    for i in range(size):
        q.dequeue()
	
    t2 = time.time()
    print("linkedListQueue.dequeuetest(): ", end="")
    print(t2 - t1)
    return










    