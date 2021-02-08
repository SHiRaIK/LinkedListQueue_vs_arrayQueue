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
        self.size += 1
    
    def dequeue(self):
        item = self.first.value
        self.first = self.first.next
        self.size -= 1
        return item
    
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
    print("LinkedListQueue.insertTest(): ", end="")
    print(t2 - t1)
    return








    