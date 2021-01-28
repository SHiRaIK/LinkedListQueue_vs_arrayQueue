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
        print("ArrayQueue created.")
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

    def size(self):
	    return len(self.items)

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
	
'''def insert(number, queue):
    q = Queue()
    inserted = False
	
    t1 = time.time()
	
    last = queue.dequeue()
    while(queue.size() > 0):
        print(queue.size())
        q.enqueue(queue.dequeue())
	
    while(q.size() > 0):
        item = q.dequeue()
        if(item < number < last or item > number > last): 
            queue.enqueue(number)
            inserted = True
        queue.enqueue(item)
        last = item
	
    t2 = time.time()
    print("arrayQueue.insert(): ", end="")
    print(t2 - t1)
    return inserted
	'''
	
	
	
	
	
    