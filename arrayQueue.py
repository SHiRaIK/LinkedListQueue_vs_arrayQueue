import time

# QueueScript slow as fuck
class QueueScript:
    def __init__(self):
        self.items = []
    
    def enqueue(self, value):
        self.items.insert(0, value)
    
    def dequeue(self):
        return self.items.pop()

class Queue:
    def __init__(self):
        self.items = []
        self.last = 0
        self.first = 0
    
    def enqueue(self, value):
        self.items.append(value)
        self.last += 1
    
    def dequeue(self):
        #self.__resize() # resize slows down
        if(self.first == self.last):
            return None
        item = self.items[self.first]
        self.first += 1
        return item

    def __resize(self):
        if(self.last - self.first <= self.first and self.first > 100):
            count = 0
            while(self.first < self.last):
                self.items[count] = self.items[self.first]
                count += 1
                self.first += 1
            self.last = self.first
            self.first = 0
            return
        else:
            return


def enqueueDequeue():
    size = 10000000
    q = Queue()

    t1 = time.time()

    for i in range(size):
        q.enqueue(i)
    
    for i in range(size):
        q.dequeue()

    t2 = time.time()
    print("ArrayQueue.enqueueDequeue(): ", end="")
    print(t2 - t1)
    return
    
    
def enqueueTest():
    size = 10000000
    q = Queue()

    t1 = time.time()
    
    for i in range(size):
        q.enqueue(i)
    
    t2 = time.time()
    print("ArrayQueue.enqueuetest(): ", end="")
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
    print("ArrayQueue.dequeuetest(): ", end="")
    print(t2 - t1)
    return
	

    