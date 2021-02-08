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
        self.size = 0
    
    def enqueue(self, value):
        self.items.append(value)
        self.last += 1
        self.size += 1
    
    def dequeue(self):
        #self.__resize() # resize slows down
        if(self.first == self.last):
            return None
        item = self.items[self.first]
        self.first += 1
        self.size -= 1
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

    def insert(self, number):
        q = Queue()
        inserted = False

        last = self.dequeue()
        while(self.size > 0):
            q.enqueue(self.dequeue())

        while(q.size > 0):
            item = q.dequeue()
            if(item < number < last or item > number > last): 
                self.enqueue(number)
                inserted = True
            self.enqueue(item)
            last = item
        return inserted

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
    print("ArrayQueue.enqueueTest(): ", end="")
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
    print("ArrayQueue.dequeueTest(): ", end="")
    print(t2 - t1)
    return
	
def insertTest():
    size = 10000000
    number = 5000000
    q = Queue()
    for i in range(size):
        if i == number:
            continue
        q.enqueue(i)
    
    t1 = time.time()
	
    q.insert(number)
	
    t2 = time.time()
    print("ArrayQueue.insertTest(): ", end="")
    print(t2 - t1)
    return
	
	
	
	
    